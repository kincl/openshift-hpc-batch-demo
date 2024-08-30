# Slurm

# Install

## Apply manifests

```
cd slurm
oc create ns slurm-system
oc apply -k manifests/
```

## Create munge secret key

```
oc -n slurm-system create secret generic munge-key --from-file=munge.key=<(dd status=none if=/dev/urandom bs=1 count=128)
```

## Create image builds

```
oc new-build --name munge --binary
oc new-build --name slurm --binary
oc new-build --name login --binary
```

```
oc start-build munge --from-dir=images/munge --follow --no-cache
oc start-build slurm --from-dir=images/slurm --follow --no-cache
oc start-build login --from-dir=images/login --follow --no-cache
```

# containerssh

```
oc new-project containerssh
```

Set your user ssh public key into the authentication app (hardcoded)

```
sed -i -e "s#ssh-rsa.*#$(cat ~/.ssh/id_rsa.pub)#" manifests/containerssh/authconfig/app.py
```

TODO: Automate or script this part
Generate host key and create a secret for it

```
openssl rsa -in mykey.pem -pubout > mykey.pub
oc create secret generic -n containerssh  containerssh-hostkey --from-file=host.key=mykey.pem
```


```
oc apply -k manifests/containerssh
```

# Checks

Check thats pods in projects `slurm-system` and `containerssh` are up and running:

```
oc get pods -n containerssh
oc get pods -n slurm-system
```

You are ready for the demo and you can return to [the main demo README](../README.md) 




