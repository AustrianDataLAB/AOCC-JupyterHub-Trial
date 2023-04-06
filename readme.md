# Deploying Jupyter

1. Verify JupyterHub settings in aocc_values.yml and fill in the placeholders for the ingress configuration.
See https://z2jh.jupyter.org/en/stable/administrator/advanced.html#ingress

2. Have a Kubernetes cluster ready, kubectl installed and kubeconfig set

3. Run the `install.sh` script

This deployment uses a DummyAuthenticator, so any username/password combination works. 

For admin rights, sign in with the `testadmin` user.

After signing in, select an image to start the Jupyter Notebook with