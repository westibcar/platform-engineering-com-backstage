### Manifesto oficial do Kubernetes Dashboard (mais recente)

Você pode aplicar diretamente com `kubectl apply`:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

Ou, se quiser o conteúdo YAML completo, aqui está (referente à versão `v2.7.0`, a mais estável até a data do meu conhecimento):

> ** ⚠️ Aviso**: O conteúdo abaixo é longo, pois inclui todos os recursos: Namespace, ServiceAccount, RoleBindings, Service, Deployment, etc.

[🔗 Link direto para visualizar no GitHub](https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml)

Se quiser, posso colar aqui o conteúdo completo, mas normalmente é mais prático usar o link acima com `kubectl apply`.


### 🔒 Acesso Seguro (Recomendações pós-deploy)

1. **Crie um ServiceAccount com permissões administrativas (opcional)**:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
```

2. **Crie um ClusterRoleBinding**:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
```

3. **Obtenha o token de login**:

```bash
kubectl -n kubernetes-dashboard create token admin-user
```

4. **Acesse o Dashboard**:

```bash
kubectl proxy
```

E depois acesse via navegador:

```
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

Sem dúvida, a maneira mais simples de instalar o Kubernetes Dashboard é por meio do Helm. Ainda assim, vou listar todas as opções disponíveis para que você possa escolher a mais adequada.

# Adicionando o repositório do kubernetes-dashboard
```
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
```
# Instale o "kubernetes-dashboard" usando helm chart
```
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```