import openai
from typing import Optional, Dict

class GPTAnalyzer:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def analyze_resume(self, resume_text: str, job_description: Optional[str] = None, role: Optional[str] = None) -> Dict:
        prompt = self._build_prompt(resume_text, job_description, role)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500  # Increased for more detailed feedback
        )
        
        return {
            "analysis": response.choices[0].message.content,
            "usage": response.usage
        }

    def _build_prompt(self, resume_text: str, job_description: Optional[str], role: Optional[str]) -> str:
        # Common instructions for all roles
        common_instructions = """
        You are a resume grader for undergraduate engineering students. Your task is to review the provided resume and give detailed feedback on:
        
        1. Content Quality:
            - Does the resume show the candidate's impact in previous roles?
            - Are achievements quantifiable and impactful?
            - Is experience and education clearly described?
            - Are key skills and certifications relevant and visible?

        2. Structure and Style:
            - Is the resume consistently formatted with appropriate font sizes and spacing?
            - Does it follow best practices in structure (header, education, experience, skills)?
            - Are there unnecessary filler words or jargon?
            - Are descriptions concise and impactful?
        
        3. General Feedback:
            - What can be improved? (Content, formatting, structure)
            - Are there missing sections or key elements?
        """
        
        # Role-specific instructions
        role_instructions = {
            'Software Engineer': """
            Technical Requirements Checklist:
            - Core Languages: Proficiency in at least 2 of (Python, Java, C++, JavaScript)
            - Development Tools: Experience with Git, CI/CD pipelines, debugging tools
            - Systems Knowledge: Understanding of algorithms, data structures, OOP principles
            - Frameworks: Experience with relevant frameworks (React, Node.js, Spring, etc.)
            - Projects: Minimum 2 substantial projects with clear technical descriptions
            
            Evaluation Focus:
            1. Code Quality Indicators:
               - Does the resume mention code reviews, testing practices, or quality metrics?
               - Are technical debt reduction or performance improvements quantified?
            2. Architecture Experience:
               - Any mention of system design, scaling, or architectural decisions?
            3. Technical Breadth:
               - Exposure to multiple parts of the stack (frontend, backend, databases)?
            """,
            
            'Data Scientist': """
            Technical Requirements Checklist:
            - Programming: Python/R with specific libraries (Pandas, NumPy, Scikit-learn)
            - Machine Learning: Experience with model development and evaluation metrics
            - Data Handling: SQL experience and big data tools (Spark, Hadoop)
            - Visualization: Tools like Matplotlib, Tableau, or Power BI
            - Projects: 2+ projects showing full ML pipeline from problem definition to deployment
            
            Evaluation Focus:
            1. Statistical Rigor:
               - Are statistical methods and assumptions properly described?
               - Is there mention of A/B testing or experimental design?
            2. Business Impact:
               - Are model improvements tied to business metrics (e.g., "improved conversion by 15%")?
            3. Production Experience:
               - Any experience deploying models (Docker, APIs, cloud services)?
            """,
            
            'DevOps Engineer': """
            Technical Requirements Checklist:
            - Cloud Platforms: AWS/Azure/GCP certifications or project experience
            - Infrastructure as Code: Terraform, Ansible, or CloudFormation
            - CI/CD: Experience setting up pipelines (Jenkins, GitHub Actions)
            - Monitoring: Tools like Prometheus, Grafana, or Datadog
            - Security: Basic understanding of security best practices
            
            Evaluation Focus:
            1. Automation Focus:
               - Are manual processes replaced with automation solutions?
               - Any metrics on efficiency gains from automation?
            2. Incident Management:
               - Experience with on-call rotations or outage resolution?
            3. Scalability:
               - Evidence of designing scalable infrastructure solutions?
            """,
            
            'Product Manager': """
            Key Competencies Checklist:
            - Product Lifecycle: Experience with all stages from ideation to launch
            - User Research: Conducting interviews, surveys, or usability tests
            - Roadmapping: Feature prioritization frameworks (RICE, Kano)
            - Analytics: Using metrics to drive decisions (SQL, Mixpanel, Amplitude)
            - Cross-functional Leadership: Engineering, design, and business collaboration
            
            Evaluation Focus:
            1. Outcome Orientation:
               - Are features tied to measurable outcomes rather than outputs?
            2. Strategic Thinking:
               - Evidence of aligning product decisions with company strategy?
            3. Technical Depth:
               - Can discuss technical constraints with engineering teams?
            """,
            
            'UX Designer': """
            Portfolio Requirements Checklist:
            - Design Process: Evidence of user research → wireframes → prototypes → testing
            - Tools: Figma/Sketch, Adobe Creative Suite, prototyping tools
            - Accessibility: WCAG compliance or inclusive design experience
            - Metrics: Usability improvements quantified (task success rates, NPS)
            
            Evaluation Focus:
            1. User-Centered Approach:
               - How clearly are design decisions tied to user needs?
            2. Visual Communication:
               - Effectiveness of information hierarchy and visual design
            3. Technical Collaboration:
               - Experience working with developers on implementation?
            """
        }.get(role, "")
        
        
        # Build the complete prompt
        prompt = f"""{common_instructions}
        
        {role_instructions if role else ''}
        
        Resume to analyze:
        {resume_text[:5000]}
        
        {f"Job Description:\n{job_description[:2000]}" if job_description else ''}
        
        Provide your feedback in this format:
        
        ### Content Quality Evaluation
        [Detailed evaluation of content with specific examples]
        
        ### Structure and Style Evaluation
        [Detailed evaluation of formatting and organization]
        
        ### Role-Specific Evaluation
        [How well the resume matches the target role requirements]
        
        ### Overall Score (1-10)
        [Numerical score with justification]
        
        ### Specific Recommendations
        [Actionable suggestions for improvement]
        """
        
        return prompt