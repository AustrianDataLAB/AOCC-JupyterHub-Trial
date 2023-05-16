# AOCC JupyterHub Trial
## 1. Local JupyterHub deployment using DockerSpawner
(Recommended. For deploying JupyterHub using the contents of this repo in a Kubernetes cluster, see section 2.)

This JupyterHub demo uses DockerSpawner to deploy custom notebook images for the user to use.
### 1.1. Requirements:
* Have docker installed
### 1.2. Installation:

1. First create `docker network create jupyterhub`

2. Pull the images so that they can be used for the demo:
    * AOCC JupyterHub image: `docker pull ghcr.io/austriandatalab/aocc_jupyterhub:jupyterhub-trial-3.1.1`

    * AOCC Mage JupyterLab image: `docker pull ghcr.io/austriandatalab/aocc_openscience_mage:sha-55e857d`
    (note: This image may take longer to download, since it contains the 3D visualization module for JupyterLab)

2. Run the following command to start the jupyterhub container:

`docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock --net jupyterhub --name aocc-jupyterhub-trial -p 8000:8000 ghcr.io/austriandatalab/aocc_jupyterhub:jupyterhub-trial-3.1.1 jupyterhub -f /etc/jupyterhub/jupyterhub_config.py --ip 0.0.0.0 --port 8000 --DockerSpawner.image ghcr.io/austriandatalab/aocc_openscience_mage:sha-55e857d`

**Customization:** If you want to run the JupyterHub container with another JupyterLab custom image, replace the `--DockerSpawner.image` value with the desired image (example: `--DockerSpawner.image jupyter/base-notebook`)

1.3. JupyterHub should now be deployed in docker and it can be accessed on `localhost:8000`.

This deployment uses a DummyAuthenticator, so any username/password combination works. 

For admin rights, sign in with the `testadmin` user.

When prompted to enter the notebook image when spawning the server, just press enter and wait for docker to deploy the jupyter lab server.

## 2. Deployment on a Kubernetes Cluster

1. Fill the missing settings in `aocc_values.yml`. The ingress and storage need to be set depending on your actual cluster settings.
2. Run `install.sh`

### _Enjoy testing the AOCC JupyterHub!_
