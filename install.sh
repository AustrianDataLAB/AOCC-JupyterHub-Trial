#!/bin/bash

FILES=''

for f in custom/*
do
  # take action on each file. $f store current file name
  FILES="$FILES --from-file=$f "
done
echo $FILES
kubectl create ns aocc-jupyterhub-trial || echo pass
kubectl delete sa default -n aocc-jupyterhub-trial || echo pass
kubectl -n aocc-jupyterhub-trial delete configmap custom-config || echo pass
kubectl -n aocc-jupyterhub-trial create configmap custom-config $FILES

kubectl rollout restart deployments hub -n aocc-jupyterhub-trial || echo pass

kubectl apply -f aocc_values.yml
kubectl apply -f aocc_profiles.yml
kubectl apply -f rbac/pv_creator.standalone.yml
kubectl apply -f rbac/psp.standalone.yml

kubectl get configmap custom-config -n aocc-jupyterhub-trial