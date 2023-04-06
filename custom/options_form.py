from email.charset import add_alias
import os
from kubespawner.clients import shared_client, load_config

## see: https://discourse.jupyter.org/t/tailoring-spawn-options-and-server-configuration-to-certain-users/8449#solution-to-problem-1-4
async def options_form(spawner):

  group = 'hub.austrianopensciencecloud.org'
  version = 'v1alpha1'
  namespace = os.getenv('POD_NAMESPACE')
  plural = 'profiles'

  #load_config()
  api_client = shared_client('CustomObjectsApi')
  #name = auth_state.get("name", "USER")
  #spawner.log.info(f"{name}s options_form groups: {groups}")

  profile_list = []

  ## see: https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CustomObjectsApi.md
  try:
    res = await api_client.list_namespaced_custom_object(group, version, namespace, plural)
    # check for allowed groups in crd profiles
    for item in res['items']:
      profile_list.append(item['spec'])
        

  
    # add profiles from helm list
    if len(spawner.profile_list) > 0:
      for prev_profile in spawner.profile_list:
        add_profile = True
        for profile in profile_list:
          if profile['slug'] == prev_profile['slug']:
            add_profile = False
            break
        if add_profile:
          profile_list.append(prev_profile)  
      
  except Exception as e:
    spawner.log.info('### Error in options_form')
    spawner.log.error(e)

  spawner.profile_list = profile_list
  return spawner._options_form_default()