import streamlit as st
import smtplib
from email.message import EmailMessage

# ---------------- CONFIG ---------------- #
SENDER_EMAIL = "outreach@phntechnology.com"
SENDER_PASSWORD = "dnrtnhcjqmqgvlyv"

# ---------------- SMTP CONFIG ---------------- #
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587  # Outlook uses STARTTLS


PHN_LOGO_URL = "https://phn-new-website.s3.ap-south-1.amazonaws.com/assets/img/WORKSHOP+2K25/logos/PHN-+LETTER+LOGO-01+5.webp"

# ---------------- EMAIL TEMPLATES ---------------- #
def get_email_template(program, name, location=None):


    PHN_LOGO_URL = "https://phn-new-website.s3.ap-south-1.amazonaws.com/assets/img/WORKSHOP+2K25/logos/PHN-+LETTER+LOGO-02+24.webp"

    # ================= EMAIL SAFE SVG ICONS ================= #

    ICON_CHECK = """
    <svg width="16" height="16" viewBox="0 0 24 24" fill="#2563eb"
    xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:10px;">
        <path d="M9 16.2l-3.5-3.5-1.4 1.4L9 19 20.3 7.7l-1.4-1.4z"/>
    </svg>11
    """

    ICON_DOT = """
    <svg width="10" height="10" viewBox="0 0 24 24" fill="#2563eb"
    xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:12px;">
        <circle cx="12" cy="12" r="6"/>
    </svg>
    """

    ICON_STAR = """
    <svg width="14" height="14" viewBox="0 0 24 24" fill="#2563eb"
    xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:10px;">
        <path d="M12 17.3l-6.2 3.7 1.6-7.1L2 9.2l7.2-.6L12 2l2.8 6.6 7.2.6-5.4 4.7 1.6 7.1z"/>
    </svg>
    """

    ICON_ARROW = """
    <svg width="14" height="14" viewBox="0 0 24 24" fill="#2563eb"
    xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:10px;">
        <path d="M13 5l7 7-7 7M5 12h14"/>
    </svg>
    """

    # ================= PROGRAM CONFIG ================= #

    PROGRAMS = {
        "IoT": {
            "subject": "Seat Confirmed: Welcome to the Top 30 of Industrial Training Internship Program (ITIP)",
            "accent": "#2563eb",
            "pastel": "#eef4ff"
        },
        "AIML": {
            "subject": "Seat Confirmed: Welcome to the Top 30 of Industrial Training Internship Program (ITIP)",
            "accent": "#4f46e5",
            "pastel": "#f1f0ff"
        }
    }

    cfg = PROGRAMS.get(program)
    if not cfg:
        raise ValueError("Invalid program selected")

    # ================= STYLES ================= #
    base = "margin:0;padding:0;font-family:'Segoe UI', Roboto, Arial, sans-serif;background:#f4f6fb;"
    card = "max-width:760px;margin:40px auto;background:#ffffff;border-radius:18px;overflow:hidden;box-shadow:0 18px 45px rgba(0,0,0,0.08);"
    header = f"background:{cfg['accent']};padding:36px;text-align:center;"
    content = "padding:40px 36px;"
    text = "color:#1f2937;font-size:15px;line-height:1.8;margin:0 0 14px;"
    muted = "color:#6b7280;font-size:14px;"
    section = f"font-size:17px;font-weight:600;margin:30px 0 16px;padding-left:12px;border-left:4px solid {cfg['accent']};color:#111827;"
    highlight = f"background:{cfg['pastel']};padding:20px 22px;border-radius:14px;margin:26px 0;"
    divider = "border:none;border-top:1px solid #e5e7eb;margin:36px 0;"

    greeting = f"Dear {name},"

    if program == "IoT":
        body_content = f"""
        <p style="{text}">{greeting}</p>
        <p style="{text}"><strong>Congratulations.</strong></p>
        <p style="{text}">
        We are pleased to officially confirm your seat for the Industrial Training Internship Program (ITIP) in <strong>Internet of Things(IoT)</strong> at <strong>{location}</strong>.
        </p>
        <div style="{highlight}">
        <p style="{text}">This is not a routine confirmation email. You are now part of an exclusive cohort of only 30 selected candidates.</p>
        </div>
        <p style="{text}">
        Out of a large pool of applicants, you were among the few who took decisive action. In today’s competitive environment, this ability to act sets candidates apart—and it is exactly what recruiters value most.
        </p>
        <p style="{section}">By securing your seat, you have already demonstrated:</p>
        <p style="{text}">{ICON_DOT} Proactiveness</p>
        <p style="{text}">{ICON_DOT} Clear career intent</p>
        <p style="{text}">{ICON_DOT} A strong professional mindset</p>
        <p style="{text}">These are the qualities that consistently distinguish shortlisted candidates from the rest.</p>
        <p style="{section}">What This Means for You</p>
        <p style="{text}">During the ITIP journey, you will engage with:</p>
        <p style="{text}">{ICON_DOT} Industry-grade problem statements</p>
        <p style="{text}">{ICON_DOT} Practical, hands-on implementations</p>
        <p style="{text}">{ICON_DOT} Skills aligned with current recruiter expectations</p>
        <p style="{text}">{ICON_DOT} Experiences that strengthen your resume, portfolio, and professional confidence</p>
        <p style="{text}">By the end of this program, you will not just have completed an internship—you will stand out in the eyes of recruiters.</p>
        <p style="{section}">Mandatory Prerequisites (Before Program Commencement)</p>
        <p style="{text}">To ensure a smooth and productive start, all participants must complete the following prerequisites before the program begins:</p>
        <p style="{text}">{ICON_DOT} Basic knowledge of C, C++ & Python</p>
        <p style="{text}">{ICON_DOT} Familiarity with variables, loops, conditionals, and basic functions is sufficient.</p>
        <p style="{text}">{ICON_DOT} Arduino IDE (Pre-installed) — Please install and ensure it runs without errors.</p>
        <p style="{text}">These prerequisites are mandatory, as the program is designed to be fast-paced and implementation-focused from Day 1.</p>
        <p style="{section}">Referral & Group Benefits (Optional but Rewarding)</p>
        <p style="{text}">You may also refer your friends or classmates who are interested in joining the program:</p>
        <p style="{text}">{ICON_DOT} ₹500 referral reward per confirmed registration</p>
        <p style="{text}">{ICON_DOT} Special group discounts for friends joining together</p>
        <p style="{text}">For referral or group registration details, feel free to reach out to us.</p>
        <p style="{section}">What’s Next</p>
        <p style="{text}">Detailed onboarding instructions, schedules, and next steps will be shared shortly.</p>
        <p style="{text}">Upon completion of the remaining payment, your login ID and password will be shared via email, providing access to your personalized learning dashboard.</p>
        <p style="{text}">Once again, welcome to the Top 30 ITIP cohort. You have taken a significant step toward becoming the kind of candidate recruiters actively look for.</p>
        <p style="{text}">We look forward to working with you.</p>
        """

    else:  # AIML
        body_content = f"""
        <p style="{text}">{greeting}</p>
        <p style="{text}"><strong>Congratulations.</strong></p>
        <p style="{text}">
        We are pleased to officially confirm your seat for the Industrial Training Internship Program (ITIP) in <strong>Artificial Intelligence & Machine Learning(AI & ML)</strong> at <strong>{location}</strong>.
        </p>
        <div style="{highlight}">
        <p style="{text}">This is not a routine confirmation. You are now part of an exclusive cohort of only 30 selected candidates chosen from a highly competitive applicant pool.</p>
        </div>
        <p style="{text}">While many expressed interests, you took action. That single decision already places you ahead of the curve. Recruiters consistently prioritize candidates who demonstrate clarity, initiative, and commitment—qualities you have already displayed.</p>
        <p style="{section}">By confirming your seat, you have shown:</p>
        <p style="{text}">{ICON_DOT} Strong intent to build an AIML-focused career</p>
        <p style="{text}">{ICON_DOT} Willingness to invest in skill development</p>
        <p style="{text}">{ICON_DOT} The mindset required to succeed in high-impact technical roles</p>
        <p style="{section}">What This Program Means for You</p>
        <p style="{text}">Throughout the 45-day AIML journey, you will work on:</p>
        <p style="{text}">{ICON_DOT} Core AI & ML concepts with real-world relevance</p>
        <p style="{text}">{ICON_DOT} Hands-on problem-solving and implementation-focused learning</p>
        <p style="{text}">{ICON_DOT} Tools, workflows, and practices used in the industry</p>
        <p style="{text}">{ICON_DOT} Building technical depth reflected on your resume and portfolio</p>
        <p style="{section}">Mandatory Prerequisites (Before Program Commencement)</p>
        <p style="{text}">To ensure all participants start on the same footing, please complete:</p>
        <p style="{text}">{ICON_DOT} Basic Python with logical understanding</p>
        <p style="{text}">{ICON_DOT} Variables, loops, functions</p>
        <p style="{text}">{ICON_DOT} Exposure to Jupyter / Google Colab</p>
        <p style="{text}">These prerequisites are mandatory for a fast-paced, implementation-focused learning.</p>
        <p style="{section}">What’s Next</p>
        <p style="{text}">Detailed onboarding instructions, schedules, and access information will be shared shortly.</p>
        <p style="{text}">Upon completion of the remaining payment, your login ID and password will be shared, giving access to your personalized dashboard with sessions, study materials, and tasks.</p>
        <p style="{text}">Please monitor your inbox carefully for updates. Once again, welcome to the Top 30 AIML cohort. We look forward to working with you.</p>
        """

    body = f"""
    <html>
    <body style="{base}">
        <div style="{card}">
            <div style="{header}">
                <img src="{PHN_LOGO_URL}" style="height:52px;">
            </div>
            <div style="{content}">
                {body_content}
                <hr style="{divider}">
                <p style="{muted}">Regards,<br><strong>PHN Technology</strong></p>
            </div>
        </div>
    </body>
    </html>
    """
    subject = f"Seat Confirmed: Welcome to the Top 30 {program} ITIP"
    return subject, body

    # ================= AIML EMAIL ================= #

    body = f"""
    <html>
    <body style="{base}">
    <div style="{card}">

        <div style="{header}">
            <img src="{PHN_LOGO_URL}" style="height:52px;">
        </div>

        <div style="{content}">

            <p style="{text}">Dear Candidate,</p>
            <p style="{text}"><strong>Congratulations.</strong></p>

            <p style="{text}">
                 We are pleased to officially confirm your seat for the
                    <strong>Industrial Training Internship Program (ITIP)</strong> at
                    <strong>{location}</strong> in the domain <strong>AI & ML</strong>.
            </p>

            <div style="{highlight}">
                <p style="{text}">
                    {ICON_STAR}
                    This is not a routine confirmation. You are now part of an exclusive cohort of
                    only <strong>30 selected candidates</strong>.
                </p>
            </div>

            <p style="{text}">
                While many expressed interest, you took action. That decision already places you ahead
                of the curve. Recruiters prioritize candidates who show clarity, initiative, and commitment.
            </p>

            <p style="{section}">By confirming your seat, you have shown:</p>
            <p style="{text}">{ICON_CHECK} Strong intent to build an AIML-focused career</p>
            <p style="{text}">{ICON_CHECK} Willingness to invest in skill development</p>
            <p style="{text}">{ICON_CHECK} Mindset for high-impact technical roles</p>

            <p style="{section}">What This Program Means for You</p>
            <p style="{text}">{ICON_DOT} Core AI & ML concepts with real-world relevance</p>
            <p style="{text}">{ICON_DOT} Hands-on problem-solving</p>
            <p style="{text}">{ICON_DOT} Industry tools & workflows</p>
            <p style="{text}">{ICON_DOT} Strong resume & portfolio depth</p>

            <div style="{highlight}">
                <p style="{text}">
                    {ICON_ARROW}
                    By the end of the program, you will apply AIML concepts with confidence —
                    exactly what recruiters look for.
                </p>
            </div>

            <p style="{section}">Mandatory Prerequisites</p>
            <p style="{text}"><strong>AIML Program Prerequisites</strong></p>
            <p style="{text}">{ICON_DOT} Basic Python with logical understanding</p>
            <p style="{text}">{ICON_DOT} Variables, loops, functions</p>
            <p style="{text}">{ICON_DOT} Jupyter / Google Colab exposure</p>

            <p style="{section}">What’s Next</p>
            <p style="{text}">
                Detailed onboarding instructions, schedules, and access information will be shared shortly.
            </p>

            <p style="{text}">
                Once again, welcome to the Top 30 AIML cohort.
                You have taken a decisive step toward becoming a high-value candidate.
            </p>

            <p style="{text}">We look forward to working with you.</p>

            <hr style="{divider}">

            <p style="{muted}">
                Regards,<br>
                <strong>PHN Technology</strong>
            </p>

        </div>
    </div>
    </body>
    </html>
    """

    return cfg["subject"], body



# ---------------- SEND EMAIL FUNCTION ---------------- #
def send_email(to_email, subject, html_body):
    msg = EmailMessage()
    msg["From"] = f"PHN Technology <{SENDER_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content("HTML Email")
    msg.add_alternative(html_body, subtype="html")

    # Connect to Outlook SMTP with STARTTLS
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()  # Enable encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

# ---------------- STREAMLIT UI ---------------- #
st.set_page_config(page_title="PHN ITIP Mailer", page_icon="https://phn-new-website.s3.ap-south-1.amazonaws.com/assets/img/WORKSHOP+2K25/logos/PHNLOGO.webp", layout="centered")
st.title("PHN Technology – ITIP Seat Confirmation")
st.markdown("Send professional seat confirmation emails with personalized names.")

location = st.selectbox("Select Institute Location", ["IIT Jammu", "IIT Patna", "NIT Delhi"])
program = st.selectbox("Select Program", ["IoT", "AIML"])

names_input = st.text_area(
    "Enter Candidate Names (comma separated)",
    placeholder="Neha Halwai, Nikita Gogawale, ..."
)
emails_input = st.text_area(
    "Enter Candidate Emails (comma separated)",
    placeholder="neha@example.com, nikita@example.com, ..."
)

if st.button("Send Emails"):
    if not names_input.strip() or not emails_input.strip():
        st.error("Please enter both names and emails.")
    else:
        names = [n.strip() for n in names_input.split(",")]
        emails = [e.strip() for e in emails_input.split(",")]

        if len(names) != len(emails):
            st.error("Number of names and emails must match!")
        else:
            success = 0
            for name, email in zip(names, emails):
                try:
                    subject, body = get_email_template(program, name, location)
                    send_email(email, subject, body)
                    success += 1
                except Exception as e:
                    st.error(f"Failed for {email}: {e}")
            st.success(f"✅ Emails sent successfully to {success} candidates!")