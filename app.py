import streamlit as st

from src.api.football_data import (
    get_competitions,
    get_standings,
    get_matches
)

st.set_page_config(
    page_title="Football Analytics",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Football Analytics")
st.write("Dashboard d'analyse de données football.")


try:
    data = get_competitions()
    competitions = data["competitions"]

    st.subheader("Choisir une compétition")

    competition_names = [
        competition["name"]
        for competition in competitions
    ]

    selected_name = st.selectbox(
        "Compétition",
        competition_names
    )

    selected_competition = next(
        competition
        for competition in competitions
        if competition["name"] == selected_name
    )


except Exception as e:
    st.error(f"Erreur lors de la récupération des données : {e}")


st.subheader("Classement")

try:
    standings_data = get_standings(selected_competition["code"])
    standings = standings_data["standings"][0]["table"]

    table_data = []

    for team in standings:
        table_data.append({
            "Pos.": team["position"],
            "Équipe": team["team"]["name"],
            "MJ": team["playedGames"],
            "V": team["won"],
            "N": team["draw"],
            "D": team["lost"],
            "BP": team["goalsFor"],
            "BC": team["goalsAgainst"],
            "Diff.": team["goalDifference"],
            "Pts": team["points"],
        })

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:
    st.error(f"Erreur lors de la récupération du classement : {e}")


st.subheader("Matchs")

try:
    matches_data = get_matches(selected_competition["code"])
    matches = matches_data["matches"]

    matches_table = []

    for match in matches:
        home_score = match["score"]["fullTime"]["home"]
        away_score = match["score"]["fullTime"]["away"]

        matches_table.append({
            "Date": match["utcDate"][:10],
            "Équipe domicile": match["homeTeam"]["name"],
            "Score": (
                f"{home_score} - {away_score}"
                if home_score is not None
                else "-"
            ),
            "Équipe extérieure": match["awayTeam"]["name"],
            "Statut": match["status"]
        })

    st.dataframe(
        matches_table,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:
    st.error(f"Erreur lors de la récupération des matchs : {e}")