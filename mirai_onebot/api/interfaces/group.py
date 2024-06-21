from typing import List

from mirai_onebot.api.interfaces.base import (Request, RequestParams, Response,
                                              ResponseData)

__all__ = [
    "GetGroupInfoRequest", "GetGroupInfoResponse", "GetGroupInfoRequestParams", "GetGroupInfoResponseData",
    "GetGroupListRequest", "GetGroupListResponse", "GetGroupListRequestParams", "GetGroupListResponseData",
    "GetGroupMemberInfoRequest", "GetGroupMemberInfoResponse", "GetGroupMemberInfoRequestParams", "GetGroupMemberInfoResponseData",
    "GetGroupMemberListRequest", "GetGroupMemberListResponse", "GetGroupMemberListRequestParams", "GetGroupMemberListResponseData",
]

# ========= GetGroupInfo =========


class GetGroupInfoRequestParams(RequestParams):
    group_id: str


class GetGroupInfoResponseData(ResponseData):
    group_id: str
    group_name: str


class GetGroupInfoRequest(Request):
    action: str = 'get_group_info'
    params: GetGroupInfoRequestParams


class GetGroupInfoResponse(Response):
    data: GetGroupInfoResponseData

# ========= GetGroupList =========


class GetGroupListRequestParams(RequestParams):
    pass


class GetGroupListResponseData(ResponseData):
    group_list: List[GetGroupInfoResponseData]


class GetGroupListRequest(Request):
    action: str = 'get_group_list'
    params: GetGroupListRequestParams


class GetGroupListResponse(Response):
    data: GetGroupListResponseData

# ========= GetGroupMemberInfo =========


class GetGroupMemberInfoRequestParams(RequestParams):
    group_id: str
    user_id: str


class GetGroupMemberInfoResponseData(ResponseData):
    user_id: str
    user_name: str
    user_displayname: str


class GetGroupMemberInfoRequest(Request):
    action: str = 'get_group_member_info'
    params: GetGroupMemberInfoRequestParams


class GetGroupMemberInfoResponse(Response):
    data: GetGroupMemberInfoResponseData

# ========= GetGroupMemberList =========


class GetGroupMemberListRequestParams(RequestParams):
    group_id: str


class GetGroupMemberListResponseData(ResponseData):
    member_list: List[GetGroupMemberInfoResponseData]


class GetGroupMemberListRequest(Request):
    action: str = 'get_group_member_list'
    params: GetGroupMemberListRequestParams


class GetGroupMemberListResponse(Response):
    data: GetGroupMemberListResponseData

# ========= SetGroupName =========


class SetGroupNameRequestParams(RequestParams):
    group_id: str
    group_name: str


class SetGroupNameRequest(Request):
    action: str = 'set_group_name'
    params: SetGroupNameRequestParams

# ========= LeaveGroup =========


class LeaveGroupRequestParams(RequestParams):
    group_id: str


class LeaveGroupRequest(Request):
    action: str = 'leave_group'
    params: LeaveGroupRequestParams
