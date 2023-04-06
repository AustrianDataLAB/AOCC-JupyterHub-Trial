from os import access
from jupyterhub.auth import Authenticator
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import json




async def my_post_auth_hook(authenticator: Authenticator, handler, authentication):
    # failsave auth_state

    print("AUTH STATE!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    authentication['groups']= ["test_course:instructor","test_course2:instructor","test_course:student","test_course2:student"]

    roles_list = []
    for groupname in authentication['groups']:
        if ":" in groupname:
            if groupname.split(":")[-1] == 'instructor':
                role = {"name":groupname,"scopes": ['admin-ui',"list:users!group=" + ":".join(groupname.split(":")[:-1]) + ":student", 
                            "list:users!group=" + ":".join(groupname.split(":")[:-1]) +":instructor",
                            "groups!group=" + ":".join(groupname.split(":")[:-1]) +":student",
                            "groups!group=" + ":".join(groupname.split(":")[:-1]) +":instructor",
                            "read:servers!group=" + ":".join(groupname.split(":")[:-1]) +":student",
                            "read:servers!group=" + ":".join(groupname.split(":")[:-1]) +":instructor",
                            "access:servers!group=" + ":".join(groupname.split(":")[:-1]) +":student",
                            "access:servers!group=" + ":".join(groupname.split(":")[:-1]) +":instructor"],
                            "groups": [groupname]}
                roles_list.append(role)
    authentication['roles'] = roles_list 
    print("DONe", authentication['roles'])
    return authentication
