# HPC Batch on OpenShift Demo

This work is part of a survey of some of the options for running HPC batch
on OpenShift/Kubernetes.

Below are the basic steps of using each scheduler

## Slurm

We are using Slurm in conjunction with [ContainerSSH](https://containerssh.io/)

(This demo use of ContainerSSH only authenticates a single SSH public key that
must be changed in the `slurm/manifests/containerssh/authconfig/app.py` file)

### Install

See [here](./slurm/README.md)

### Demo

#### *Get the login node address and SSH*
```
oc ns slurm-system
oc get pods
oc get svc -n containerssh

ssh user1@NODE -p 2222
```

#### *Run job that requires more nodes than are available*
```
cd /home/user1/pi
sinfo -N
squeue
cat job.pbs
sbatch job.pbs
watch 'squeue;sinfo -N'
```

#### *Scale Slurm node pool*
```
oc scale statefulset/compute --replicas=2
```

## Fluence

This example uses Fluence as a secondary scheduler in OpenShift as well as the MPIJob
Operator to run a simple MPI pi application

### Demo

```
oc ns default
cd ~/work/hpc/fluence
oc get nodes | grep worker | sort
cat simple-pi.yaml
oc create -f simple-pi.yaml
oc get pods -o wide -n default --sort-by=.spec.nodeName

cat simple-pi-fluence.yaml
oc create -f simple-pi-fluence.yaml
oc get pods -o wide -n default --sort-by=.spec.nodeName -l app=fluence-pi
```

## Kueue

Use kueue to run a simple job

### Demo

```
oc ns default
cd ~/work/hpc/kueue
cat single-clusterqueue-setup.yaml
cat simple-job.yaml
oc create -f simple-job.yaml

oc get pods -o wide -n default --sort-by=.spec.nodeName
```

## Flux-operator

### Install

#### Deploy MiniCluster

```
oc ns flux-operator
oc get pods -n operator-system
cd ~/work/hpc/flux/flux-operator
cat config/samples/flux-framework.org_v1alpha1_minicluster.yaml
oc create -f config/samples/flux-framework.org_v1alpha1_minicluster.yaml
oc logs flux-sample-0-
```

### Demo

Run job from the web UI http://flux-flux-operator.apps.(cluster address)

```
Command:  lmp -v x 2 -v y 2 -v z 2 -in in.reaxc.hns -nocite
Work Dir: /home/flux/examples/reaxff/HNS
```
