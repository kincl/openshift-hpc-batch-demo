FROM quay.io/containerssh/agent AS agent

FROM image-registry.openshift-image-registry.svc:5000/slurm-system/slurm:latest

COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent

