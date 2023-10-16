import json
from typing import Type

import requests
import streamlit as st
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from requests.auth import HTTPBasicAuth


class NoOpTool(BaseTool):
    name = "noop"
    description = "Don't call this tool"

    def _run(self, query):
        return "noop"


class ToggleLightInput(BaseModel):
    on: bool = Field(description="Whether to turn the light on or off")


class ToggleStreamlitImageLightTool(BaseTool):
    name = "toggle-light"
    description = "toggle the light on or off"
    args_schema: Type[BaseModel] = ToggleLightInput

    def _run(self, on):
        st.session_state.is_light_on = on
        return json.dumps({"is_light_on": on})


class ToggleFanInput(BaseModel):
    on: bool = Field(description="Whether to turn the fan on or off")


class ToggleStreamlitImageFanTool(BaseTool):
    name = "toggle-fan"
    description = "toggle the fan on or off"
    args_schema: Type[BaseModel] = ToggleFanInput

    def _run(self, on):
        st.session_state.is_fan_on = on
        return json.dumps({"is_fan_on": on})


def get_streamlit_image_tools() -> list[BaseTool]:
    return [
        ToggleStreamlitImageLightTool(),
        ToggleStreamlitImageFanTool(),
    ]


class ToogleRemoteLightTool(BaseTool):
    name = "toggle-light"
    description = "toggle the light on or off"
    args_schema: Type[BaseModel] = ToggleLightInput

    host: str
    room_id: str
    basic_auth_username: str
    basic_auth_password: str

    def _run(self, on):
        url = f"http://{self.host}/rooms/{self.room_id}/update"
        auth = HTTPBasicAuth(self.basic_auth_username, self.basic_auth_password)
        req_body = {"is_light_on": on}
        res = requests.post(url, auth=auth, json=req_body)
        return res.text


class ToogleRemoteFanTool(BaseTool):
    name = "toggle-fan"
    description = "toggle the fan on or off"
    args_schema: Type[BaseModel] = ToggleFanInput

    host: str
    room_id: str
    basic_auth_username: str
    basic_auth_password: str

    def _run(self, on):
        url = f"http://{self.host}/rooms/{self.room_id}/update"
        auth = HTTPBasicAuth(self.basic_auth_username, self.basic_auth_password)
        req_body = {"is_fan_on": on}
        res = requests.post(url, auth=auth, json=req_body)
        return res.text


def get_remote_room_tools(
    host: str,
    room_id: str,
    basic_auth_username: str = "testuser",
    basic_auth_password: str = "testpassword",
) -> list[BaseTool]:
    return [
        ToogleRemoteLightTool(
            host=host,
            room_id=room_id,
            basic_auth_username=basic_auth_username,
            basic_auth_password=basic_auth_password,
        ),
        ToogleRemoteFanTool(
            host=host,
            room_id=room_id,
            basic_auth_username=basic_auth_username,
            basic_auth_password=basic_auth_password,
        ),
    ]
