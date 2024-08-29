import json
from starlette.requests import Request
from typing import Any, Callable, Dict, List, Optional

class State:
    def __init__(self, request: Request) -> None:
        self._state_: Dict[str, Any] = self._get_state_(request)
        self._hx_req_info_: Dict[str, Any] = self._get_hx_info_(request)
        self._hx_modifier_: Dict[str, Any] = {}

    def _get_state_(self, request: Request) -> Dict[str, Any]:
        return json.loads(request.headers.get("X-Component-State", "{}"))
    
    def _get_hx_info_(self, request: Request) -> Dict[str, Any]:
        hx_info = {}
        hx_info['prompt'] = request.headers.get("HX-Prompt", None)
        hx_info['trigger'] = request.headers.get("HX-Trigger", None)
        hx_info['boosted'] = request.headers.get("HX-Boosted", None)
        hx_info['current_url'] = request.headers.get("HX-Current-URL", None)
        hx_info['trigger_name'] = request.headers.get("HX-Trigger-Name", None)
        hx_info['history_restore_request'] = request.headers.get("HX-History-Restore-Request", None)
        hx_info['target'] = [t for t in request.headers.get("HX-Target", "").split(" ") if t.strip() != ""]
        return hx_info

    def get_state(self) -> Dict[str, Any]:
        return self._state_

    def set(self, key: str, value: Any) -> None:
        self._state_[key] = value

    def update_state(self, updates: Dict[str, Any]) -> None:
        self._state_.update(updates)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self._state_.get(key, default)
    
    def get_trigger(self) -> str|None:
        return self._hx_req_info_.get("trigger", None)
    
    def get_target(self) -> str:
        return ''.join(self._hx_req_info_.get("target", []))
    
    def reswap(self, swap: str) -> str:
        self._hx_modifier_['HX-Reswap'] = swap
        return swap
    
    def retarget(self, targets: List[str]) -> str:
        self._hx_modifier_['HX-Retarget'] = ' '.join(targets)
        return self._hx_modifier_['HX-Retarget']
    
    def update_target(self, prev_target:str, new_target: str) -> dict:
        retarget: dict = self._hx_modifier_.get('HX-Target-Update', {})
        retarget.update({prev_target: new_target})
        self._hx_modifier_['HX-Target-Update'] = retarget
        return retarget
    
    def trigger_event(self, trigger: Dict[str, Any]) -> str|dict:
        events = []
        string_type_trigger = True
        for k, v in trigger.items():
            events.append(k)
            if v:
                string_type_trigger = False
                if v is None:
                    trigger[k] = {}
        if string_type_trigger:
            self._hx_modifier_['HX-Trigger'] = ', '.join(events)
            return self._hx_modifier_['HX-Trigger']
        self._hx_modifier_['HX-Trigger'] = trigger
        return self._hx_modifier_['HX-Trigger']
    
    def get_response_modifier(self) -> Dict[str, Any]|None:
        modifier = {}
        if self._hx_modifier_:
            modifier.update({k: json.dumps(v) for k, v in self._hx_modifier_.items()})
        if self._state_:
            modifier['X-Component-State'] = json.dumps(self._state_)
            modifier['HX-Trigger-Id'] = self.get_trigger()
        return modifier if modifier else None
        