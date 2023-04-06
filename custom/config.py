from .post_auth_hook import my_post_auth_hook
from jupyterhub.auth import DummyAuthenticator
from .options_form import options_form

def setup_hub(c):
  c.Application.log_level = 'DEBUG'

  c.JupyterHub.authenticator_class = DummyAuthenticator
  
  # users in `admin_group` group will be marked as admin
  c.DummyAuthenticator.admin_users= ["testadmin"]
  c.DummyAuthenticator.refresh_pre_spawn = True
  c.DummyAuthenticator.enable_auth_state = True
  c.DummyAuthenticator.manage_groups = True
  c.DummyAuthenticator.manage_roles = True


 

  ####################
  ### CUSTOM HOOKS ###
  ####################

  c.DummyAuthenticator.post_auth_hook = my_post_auth_hook
 
  c.KubeSpawner.options_form = options_form
