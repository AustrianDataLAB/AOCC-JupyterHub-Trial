# Deploying Jupyter

1. Verify JupyterHub settings in aocc_values.yml and fill in the placeholders for the ingress configuration, as well as the storage class (if necessary).
See https://z2jh.jupyter.org/en/stable/administrator/advanced.html#ingress

2. Have a Kubernetes cluster ready, kubectl installed and kubeconfig set.

3. Run the `install.sh` script. This will create a namespace from scratch and install the required custom resources, as well as the helm chart with the custom AOCC JupyterHub  image.

This deployment uses a DummyAuthenticator, so any username/password combination works. 

For admin rights, sign in with the `testadmin` user.

After signing in, select an image to start the Jupyter Notebook with