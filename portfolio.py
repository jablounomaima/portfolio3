import streamlit as st

# --- CONFIGURATION GLOBALE ---
st.set_page_config(page_title="Portfolio - Étudiant en Génie Logiciel", layout="wide")

# --- MENU LATERAL ---
pages = ["🏠 Accueil", "👨‍💻 Profil Technique", "🛠️ Stack & Compétences", "📊 Réalisations", "📬 Contact", "📄 Télécharger mon CV"]
choice = st.sidebar.radio("Navigation", pages)

# --- PAGES ---
if choice == "🏠 Accueil":
    st.title("🚀 Portfolio - Ingénieur en Génie Logiciel")
    st.write("""
    Étudiant en Génie Logiciel | Développeur Full-Stack | Junior Data Engineer
    """)

elif choice == "👨‍💻 Profil Technique":
    st.header("Profil Technique")
    st.write("""
    - Conception et développement d’applications **Web** avec Django (Python) et PHP.  
    - Déploiement et administration sur systèmes **Linux (Ubuntu, Kali Linux)**.  
    - Intégration de modèles d’**IA légère** pour la prévision et l’analyse décisionnelle.  
    """)

elif choice == "🛠️ Stack & Compétences":
    st.header("🛠️ Stack & Compétences")

    st.subheader("Langages de programmation")
    st.write("Python | PHP | JavaScript")

    st.subheader("Bases de données & Requêtes")
    st.write("SQL (MySQL, PostgreSQL, SQLite)")

    st.subheader("Frameworks & Bibliothèques")
    st.write("Django | Flask | Streamlit | Bootstrap")

    st.subheader("Data Science & IA")
    st.write("Pandas | NumPy | Scikit-learn | Prophet | Visualisation (Matplotlib, Seaborn)")

    st.subheader("DevOps & Systèmes")
    st.write("Linux (Ubuntu, Kali) | Docker | Git/GitHub | CI/CD")


elif choice == "📊 Réalisations":
    st.header("Réalisations (Projects)")

        # Projet 3 - Système de Réservation pour Clinique Vétérinaire
    st.subheader("🐾 Système de Réservation en Ligne - Clinique Vétérinaire")
    st.write("""
    Application web complète permettant aux clients de :
    - Créer un compte personnel sécurisé.
    - Enregistrer leurs animaux (nom, espèce, race, date de naissance).
    - Prendre rendez-vous en ligne (consultations, vaccinations, etc.).
    - Consulter l’historique de leurs rendez-vous.
    - Télécharger le dossier médical de leur animal au format PDF.
    - Gérer leurs demandes (annulation, modification).

    **Interface d’administration pour le personnel vétérinaire :**
    - Valider ou refuser les rendez-vous.
    - Consulter toutes les fiches animales.
    - Filtrer les RDV par statut, date ou utilisateur.
    - Gérer les comptes utilisateurs.
    """)

    st.markdown("**Technologies utilisées :**")
    st.write("""
    - **Langage** : Python 3.12  
    - **Framework** : Django 5.2  
    - **Base de données** : SQLite (développement) → PostgreSQL (production future)  
    - **Frontend** : HTML / CSS / Bootstrap 5 (design responsive)  
    - **Authentification** : django-allauth (locale + Google)  
    - **PDF** : WeasyPrint (génération de dossiers médicaux)  
    - **DevOps** : Git / GitHub (gestion de version)  
    """)


    if st.button("Voir captures - Réservation Vétérinaire"):
         st.video("assets/vedio_vet.mp4", format="video/mp4", start_time=0)


  
    # Projet 2 - PharmaInsight
    st.subheader("💊 PharmaInsight (Streamlit + Python)")
    st.write("""
    Tableau de bord analytique pour la parapharmacie Pharmavie :
    - Prévisions de ventes
    - Recommandation de produits
    - Détection automatique de ruptures de stock
    - Identification des produits phares
    """)

    if st.button("Voir captures - PharmaInsight"):
        st.image("assets/bi/2.png", caption="Dashboard accueil", use_column_width=True)
        st.image("assets/bi/3.png", caption="Graphiques ventes", use_column_width=True)
        st.image("assets/bi/4.png", caption="Graphiques ventes", use_column_width=True)
        st.image("assets/bi/5.png", caption="Graphiques ventes", use_column_width=True)
        st.image("assets/bi/6.png", caption="Graphiques ventes", use_column_width=True)
        st.image("assets/bi/7.png", caption="Graphiques ventes", use_column_width=True)

elif choice == "📬 Contact":
    st.header("Contact Professionnel")
    st.write("📧 Email : jabloun.omaima5102000@gmail.com")
    st.write("💼 LinkedIn : [https://www.linkedin.com/in/jabloune-oumayma-b064aa355/](https://linkedin.com)")
    st.write("🐙 GitHub : [https://github.com/jablounomaima](https://github.com)")

elif choice == "📄 Télécharger mon CV":
    st.header("Télécharger mon CV")
    with open("assets/cv.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Télécharger mon CV",
            data=pdf_file,
            file_name="CV_Oumaima.pdf",
            mime="application/pdf"
        )
