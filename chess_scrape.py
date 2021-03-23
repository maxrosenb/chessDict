import requests
import json
import re
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Glossary_of_chess")
soup = BeautifulSoup(open("better_glossary.html"), "html.parser")
dts = soup.find_all("dt")
dds = soup.find_all("dd")
chess_dict = {}
for i, dt in enumerate(dts):
    term = dt.text
    definition = dds[i].text
    definition = re.sub("\\[.*\\]", "", definition)
    chess_dict[term] = definition

chess_dict[
    "zugzwang "
] = "[from German, 'compulsion to move'] When a player is put at a disadvantage by having to make a move; where any legal move weakens the position."
chess_dict[
    "zwischenschach "
] = "[from German, 'in-between check'] Playing a surprising check that the opponent did not consider when plotting a sequence of moves"
chess_dict[
    "zwischenzug "
] = "[from German, 'in-between move'] An 'inbetween' move, or an Intermezzo, played before an expected reply"

with open("chess_glossary.json", "w") as outfile:
    json.dump(chess_dict, outfile)