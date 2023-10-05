import json
from typing import Type

import requests
import streamlit as st
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field


class ToggleLightInput(BaseModel):
    on: bool = Field(description="Whether to turn the light on or off")


class ToggleStreamlitLightTool(BaseTool):
    name = "toggle-light"
    description = "toggle the light on or off"
    args_schema: Type[BaseModel] = ToggleLightInput

    def _run(self, on):
        st.session_state.is_light_on = on
        return json.dumps({"is_light_on": on})


class ToogleRemoteLightTool(BaseTool):
    name = "toggle-light"
    description = "toggle the light on or off"
    args_schema: Type[BaseModel] = ToggleLightInput

    host = "localhost"
    room_id: str

    def _run(self, on):
        url = f"http://{self.host}/rooms/{self.room_id}/update"
        req_body = {"is_light_on": on}
        res = requests.post(url, json=req_body)
        return res.text


class ToggleFanInput(BaseModel):
    on: bool = Field(description="Whether to turn the fan on or off")


class ToggleStreamlitFanTool(BaseTool):
    name = "toggle-fan"
    description = "toggle the fan on or off"
    args_schema: Type[BaseModel] = ToggleFanInput

    def _run(self, on):
        st.session_state.is_fan_on = on
        return json.dumps({"is_fan_on": on})
