import streamlit as st
import smtplib
from email.message import EmailMessage

# ---------------- CONFIG ---------------- #
SENDER_EMAIL = "nehahalwai75@gmail.com"
SENDER_PASSWORD = "hfic mcog vcso nakr"

PHN_LOGO_URL = "https://phn-new-website.s3.ap-south-1.amazonaws.com/assets/img/WORKSHOP+2K25/logos/PHN-+LETTER+LOGO-01+5.webp"

# ---------------- EMAIL TEMPLATES ---------------- #
def get_email_template(program, location=None):

    PHN_LOGO_URL = "https://phn-new-website.s3.ap-south-1.amazonaws.com/assets/img/WORKSHOP+2K25/logos/PHN-+LETTER+LOGO-02+24.webp"

    # ================= EMAIL SAFE SVG ICONS ================= #

    ICON_CHECK = """
    <svg width="16" height="16" viewBox="0 0 24 24" fill="#2563eb"
    xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:10px;">
        <path d="M9 16.2l-3.5-3.5-1.4 1.4L9 19 20.3 7.7l-1.4-1.4z"/>
    </svg>
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

    base = """
    margin:0;
    padding:0;
    background:#f4f6fb;
    font-family:'Segoe UI', Roboto, Arial, sans-serif;
    """

    card = """
    max-width:760px;
    margin:40px auto;
    background:#ffffff;
    border-radius:18px;
    overflow:hidden;
    box-shadow:0 18px 45px rgba(0,0,0,0.08);
    """

    header = f"""
    background:{cfg['accent']};
    padding:36px;
    text-align:center;
    """

    content = "padding:40px 36px;"
    text = "color:#1f2937;font-size:15px;line-height:1.8;margin:0 0 14px;"
    muted = "color:#6b7280;font-size:14px;"

    section = f"""
    font-size:17px;
    font-weight:600;
    margin:30px 0 16px;
    padding-left:12px;
    border-left:4px solid {cfg['accent']};
    color:#111827;
    """

    highlight = f"""
    background:{cfg['pastel']};
    padding:20px 22px;
    border-radius:14px;
    margin:26px 0;
    """

    divider = f"""
    border:none;
    border-top:1px solid #e5e7eb;
    margin:36px 0;
    """

    # ================= IOT EMAIL ================= #

    if program == "IoT":

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
                    <strong>{location}</strong> in the domain <strong>IoT</strong>.
                </p>

                <div style="{highlight}">
                    <p style="{text}">
                        {ICON_STAR}
                        This is not a routine confirmation email. You are now part of an
                        exclusive cohort of only <strong>30 selected candidates</strong>.
                    </p>
                </div>

                <p style="{text}">
                    Out of a large pool of applicants, you were among the few who took decisive action.
                    In today’s competitive environment, this ability to act sets candidates apart—and
                    it is exactly what recruiters value most.
                </p>

                <p style="{section}">By securing your seat, you have already demonstrated:</p>
                <p style="{text}">{ICON_CHECK} Proactiveness</p>
                <p style="{text}">{ICON_CHECK} Career intent</p>
                <p style="{text}">{ICON_CHECK} A strong professional mindset</p>

                <p style="{text}">
                    These are the qualities that consistently distinguish shortlisted candidates from the rest.
                </p>

                <p style="{section}">What This Means for You</p>
                <p style="{text}">{ICON_DOT} Industry-grade problem statements</p>
                <p style="{text}">{ICON_DOT} Practical, hands-on implementations</p>
                <p style="{text}">{ICON_DOT} Skills aligned with current recruiter expectations</p>
                <p style="{text}">{ICON_DOT} Experiences that strengthen your resume, portfolio, and confidence</p>

                <div style="{highlight}">
                    <p style="{text}">
                        {ICON_ARROW}
                        By the end of this program, you will not just have completed an internship —
                        <strong>you will stand out in the eyes of recruiters.</strong>
                    </p>
                </div>

                <p style="{section}">Mandatory Prerequisites</p>
                <p style="{text}"><strong>IoT Track Prerequisites</strong></p>
                <p style="{text}">{ICON_DOT} Basic knowledge of Python</p>
                <p style="{text}">{ICON_DOT} Familiarity with variables, loops, conditionals, and functions</p>
                <p style="{text}">{ICON_DOT} Arduino IDE pre-installed and running without errors</p>

                <p style="{text}">
                    These prerequisites are mandatory, as the program is fast-paced and
                    implementation-focused from Day 1.
                </p>

                <p style="{section}">What’s Next</p>
                <p style="{text}">
                    Detailed onboarding instructions, schedules, and next steps will be shared shortly.
                </p>

                <p style="{text}">
                    Once again, welcome to the Top 30 ITIP cohort.
                    You have taken a significant step toward becoming the kind of candidate recruiters actively look for.
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

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="PHN ITIP Mailer", page_icon="📧", layout="centered")

st.title(" PHN Technology – ITIP Seat Confirmation")
st.markdown("Send professional seat confirmation emails in one click.")

location = st.selectbox(
    "Select Institute Location",
    ["IIT Jammu", "IIT Patna", "NIT Delhi"]
)

program = st.selectbox(
    "Select Program",
    ["AIML", "IoT"]
)

emails = st.text_area(
    "Enter Candidate Email IDs (comma separated)",
    placeholder="example1@gmail.com, example2@gmail.com"
)

if st.button(" Send Emails"):
    if not emails.strip():
        st.error("Please enter at least one email ID.")
    else:
        email_list = [e.strip() for e in emails.split(",")]
        subject, body = get_email_template(program, location)

        success = 0
        for email in email_list:
            try:
                send_email(email, subject, body)
                success += 1
            except Exception as e:
                st.error(f"Failed for {email}: {e}")

        st.success(f"✅ Emails sent successfully to {success} candidates!")
