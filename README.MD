## Jenkins

[https://plugins.jenkins.io/kubernetes/](https://plugins.jenkins.io/kubernetes/)


For setting up Kubernetes as a jenkins cluster cloud provider,
[https://itnext.io/dynamic-jenkins-agent-from-kubernetes-4adb98901906](https://itnext.io/dynamic-jenkins-agent-from-kubernetes-4adb98901906)

Once the plugin is installed - we need to connect to the kubernetes cluster
Go to Manage Jenkins → Manage Nodes and Clouds → Configure Clouds

Create a new cloud configuration with Kubernetes.

On the kubernetes server - The service account can be created with this yaml file - Service account (https://gecgithub01.walmart.com/s0c0a35/sup-docker-files/blob/master/kubernetes/jenkins-service-aaount.yaml)

Follow this documentation from cloudbees for the setup of service accounts and kubernetes connection

Fill the configuration as explained in the website [https://itnext.io/dynamic-jenkins-agent-from-kubernetes-4adb98901906](https://itnext.io/dynamic-jenkins-agent-from-kubernetes-4adb98901906), production setup values for your reference,
get the server certificate key -

```
root@node1:/mnt/portal/sup-docker-files/kubernetes $ kubectl get secrets
NAME                                TYPE                                  DATA   AGE
api-server-secrets                  Opaque                                13     78m
cockroach-database-sa-token-jq5dz   kubernetes.io/service-account-token   3      4m48s
cockroach-operator-sa-token-x89z4   kubernetes.io/service-account-token   3      4m47s
dashboard-tls-secrets               kubernetes.io/tls                     3      56m
default-token-d48ln                 kubernetes.io/service-account-token   3      80m
jenkins-token-jrmbq                 kubernetes.io/service-account-token   3      54m
mongo-express-credentials           Opaque                                2      78m
mongo-secret-key                    Opaque                                1      78m
mongo-sup-credentials               Opaque                                2      78m
 
# Getting the secret name as jenkins-token-jrmbq
 
kubectl get secrets jenkins-token-jrmbq -o yaml
 
# Decoding the tokens from secrets
 
echo "<token data from the yaml output>" | base64 --decode
echo "<ca.crt data from the yaml output>" | base64 --decode
```
