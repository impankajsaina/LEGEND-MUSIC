#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "26144852")
        self.API_HASH: str = os.environ.get("API_HASH", "f437972ec6dd0bd5e34599d9e83ee9ad")
        self.SESSION: str = os.environ.get("SESSION", "AQGO8FQAJAG34VIU4l2xrfsDNFbTh6dcaQSoHCoe7vB_tP_t-UaKYXiMRp3zz-ECsKadoAzjE1Qr9m6ph3ozO76Qr6wstgljM5KPdckogIOXWhrBRcesQUl36OrBMdtXD542_Maweq3dH9V9bP5cMMa2bbrsyFgrCZGw2ABw2LUkCsFFX1PRoZY8ThWwqewDTIFsFsCHLlNsVyXcoIipQDAAx670zLA5aX-hR2f7v1yn_sEJc29R_y_P_vqQpK02XEMZ15zoqmqrOkNS9104ntNAM0N4fhc7d5g4m4VsNGgSzi7grkujVNKDqUbA6PDNyET0C7NakYI8mj0uaYA0BwVwxhZzPgAAAAFXjnDzAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5831028973:AAFVHD4asdU66UHon-pmNegB-EhQy63z8us")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "1798996963").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "video")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
