# Copyright (c) 2021 Itz-fork
# Part of: Nexa-Userbot

import os

class Config(object):
    APP_ID = os.environ.get("APP_ID", "2620528")
    API_HASH = os.environ.get("API_HASH", "214facffc9dfa53e572ca822409d1569")
    # Pyrogram Session
    PYRO_STR_SESSION = os.environ.get("PYRO_STR_SESSION", "BQAib6IwoeNGD4WVS5aI-1H7McyUIvvh7UPzS9EdTcc9JshNQMGxCJxdKvIzmFipRutUfcQ5unAZ5l3i1PEJStjzhLsFqcvU2za21HNBzjTwlAQ6isO5jOY7ZILabZXp0bt3iwpeWDxjSX0RXZDpiVdEbPIb1pSs8tQP4hZmDwMaSzJD8yzGD_9WeGXLlxtUhndf3zCpQtaEGixca6vAF-R67au7x1E1jiIbHZY1wF3uSJyZL_A01QKztwTkMZS1mqyJOxTr_qewjmYNpEu6aSlzgKqlKuQYDMh2b735SeuY4jORfCZU2r0TRqx7-zFh9OkEBPGxWT2Zu5-NZ8ZXU07PTCmoewA")
    CMD_PREFIX = os.environ.get("CMD_PREFIX", "-")
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://Thor:Thor@thor.r2sge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
