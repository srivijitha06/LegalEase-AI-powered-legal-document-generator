import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap'
        );

        .stApp {

            background:
            linear-gradient(
                135deg,
                #FFFDF8 0%,
                #F5F0FA 50%,
                #EEF8F7 100%
            );

            color: #263238;

            font-family:
            'DM Sans',
            sans-serif;
        }

        .block-container {

            max-width: 1300px;

            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {

            padding: 2.5rem;

            border-radius: 30px;

            background:
            linear-gradient(
                120deg,
                #EDE7F6,
                #E3F2FD,
                #FFF3E8
            );

            border: 1px solid #DDD5E7;

            box-shadow:
            0 20px 45px
            rgba(70, 60, 90, .10);

            margin-bottom: 1.5rem;
        }

        .logo {

            font-family:
            'Playfair Display',
            serif;

            font-size: 3.4rem;

            font-weight: 700;

            color: #56466F;
        }

        .tagline {

            color: #607D8B;

            font-size: 1.05rem;
        }

        .badge {

            display: inline-block;

            padding:
            .4rem .8rem;

            border-radius: 999px;

            background: #FFFFFFAA;

            border:
            1px solid #D7CDE4;

            color: #65577C;

            font-size: .75rem;

            font-weight: 700;
        }

        .card {

            background:
            rgba(255,255,255,.78);

            border:
            1px solid #DDDDE5;

            border-radius: 22px;

            padding: 1.4rem;

            box-shadow:
            0 10px 30px
            rgba(60,60,80,.06);

            margin-bottom: 1rem;
        }

        .card-title {

            font-family:
            'Playfair Display',
            serif;

            font-size: 1.4rem;

            color: #56466F;

            font-weight: 700;
        }

        .metric {

            background:
            rgba(255,255,255,.75);

            border:
            1px solid #DEDCE6;

            border-radius: 18px;

            padding: 1rem;

            text-align: center;
        }

        .metric-number {

            font-size: 1.5rem;

            color: #67577D;

            font-weight: 700;
        }

        .metric-label {

            color: #78909C;

            font-size: .78rem;
        }

        div.stButton > button {

            border-radius: 13px;

            border:
            1px solid #CEC4DC;

            background: #EEE8F6;

            color: #54456C;

            font-weight: 700;

            min-height: 2.8rem;
        }

        div.stButton > button:hover {

            background: #E1D9EE;

            border-color: #AFA1C0;
        }

        .document {

            background: #FFFDF8;

            border:
            1px solid #DED6C9;

            border-radius: 20px;

            padding: 1.8rem;

            font-family:
            Georgia,
            serif;

            line-height: 1.8;

            min-height: 400px;

            box-shadow:
            inset 0 0 25px
            rgba(100,80,50,.03);
        }

        .footer {

            text-align: center;

            color: #78909C;

            padding: 2rem;

            font-size: .78rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )