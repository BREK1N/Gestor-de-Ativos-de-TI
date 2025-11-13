# Gestor de Ativos de TI
Gestor de Ativos de TI Basico feito em Django exercicio


Finalizamos a fase teórica de Python e SQL. Agora, iniciamos a capacitação prática para nivelamento e preparação para o projeto principal.

Nosso primeiro projeto será construir um "Gestor de Ativos de TI". O objetivo é construir um mini-sistema completo (com front-end) onde um usuário possa cadastrar, listar e ver detalhes de equipamentos.

Vocês deverão pesquisar e implementar a melhor forma de atingir esses objetivos usando a documentação do Django e outras fontes.

📋 Objetivos e Funcionalidades Requeridas
O projeto deve ser um aplicativo web funcional que permita as seguintes ações sem usar a tela /admin:

Cadastrar um Equipamento: O usuário deve ter uma página com um formulário para inserir novos equipamentos.

Listar Equipamentos: O usuário deve ter uma página principal que mostre todos os equipamentos cadastrados.

Ver Detalhes: Na página de listagem, o usuário deve poder clicar em um equipamento para ver uma página separada com todos os detalhes daquele item.

Navegação: A navegação entre essas páginas (Lista -> Detalhe, Lista -> Cadastro, Cadastro -> Lista) deve ser fluida e feita por links ou redirecionamentos.

🧩 Roteiro de Desenvolvimento
Aqui estão as etapas macro que vocês devem seguir. O "como" fazer cada etapa é parte do desafio e do aprendizado.

Etapa 1: Configuração do Projeto
Vocês deverão iniciar um novo projeto Django.

É obrigatório o uso de um ambiente virtual (como o venv) para gerenciar as dependências do projeto.

Instalem o Django e não se esqueçam de gerar e manter atualizado o arquivo requirements.txt.

Estruturem o projeto com um app principal (ex: inventario) e lembrem-se de registrá-lo no INSTALLED_APPS.

Etapa 2: Models (A Base de Dados)
No models.py do app inventario, vocês vão definir a estrutura do banco. Precisamos de dois models:

1. Categoria: Deve ter, no mínimo, um campo para o nome (ex: "Notebooks", "Monitores").

2. Equipamento: Este é o model principal. Pensem em quais campos ele precisa. Sugestões:

Nome do equipamento.

Número de serial (como garantir que ele seja único?).

Data de aquisição.

Um campo de status (pesquisem como usar a opção choices para limitar os valores a "Em Uso", "Estoque", "Manutenção").

Um relacionamento que ligue cada Equipamento a uma Categoria (pesquisem sobre ForeignKey e suas opções, como on_delete).

Lembrem-se de adicionar o método _str_ em ambos os models para facilitar a visualização.

Etapa 3: Migrations e Validação no Admin
Após definir os models, gerem e apliquem as migrações (makemigrations, migrate).

Crie um superusuário para acessar o painel de administração.

Registre seus models no admin.py.

Teste de Validação: Antes de ir para o front-end, acessem o /admin e tentem cadastrar manualmente algumas categorias e equipamentos. Se funcionar, seus models estão corretos e prontos.

Etapa 4: Formulários (O "C" do CRUD)
Para que o usuário possa cadastrar equipamentos pelo site, vocês precisarão de formulários.

Pesquisem sobre o django.forms. A abordagem mais eficiente aqui é usar ModelForm.

Criem um arquivo forms.py no app inventario e definam o formulário de cadastro de Equipamento.

Etapa 5: Views e Templates (O "V" e "T")
Esta é a lógica principal do aplicativo. No views.py, vocês precisarão criar as views (sejam funções ou classes) para:

1. View de Listagem: Deve buscar todos os equipamentos do banco e enviá-los para um template HTML.

2. View de Detalhe: Deve receber um ID (ou slug) pela URL, buscar um equipamento específico e enviá-lo para um template de detalhe.

3. View de Cadastro: Esta é a mais complexa. Ela precisa lidar com dois métodos HTTP:

GET: Deve apenas exibir o ModelForm (vazio) para o usuário preencher.

POST: Deve pegar os dados enviados, validar o formulário (form.is_valid()), salvar no banco se estiver tudo certo, e então redirecionar o usuário para outra página (ex: a lista de equipamentos).

Criem os arquivos HTML correspondentes para cada uma dessas views.

Etapa 6: URLs (A Navegação)
Configurem os arquivos urls.py (tanto o do projeto principal quanto o do app inventario).

Vocês precisam definir as rotas (URLs) que apontam para cada uma das três views que vocês criaram.

🤖 Diretrizes sobre o Uso de Inteligência Artificial
Vocês podem e devem usar ferramentas de IA (como o Gemini, ChatGPT, etc.) como apoio, mas com regras claras. O objetivo é que vocês aprendam, e não que a IA faça o projeto.

✅ PERMITIDO:

Tirar dúvidas conceituais: "Qual a diferença entre ForeignKey e ManyToManyField?", "Como funciona um ModelForm?", "O que faz o form.is_valid()?".

Ajudar a depurar (debugar) erros: Colar o seu código e o erro e perguntar "O que significa este erro: NoReverseMatch e como posso corrigi-lo?".

Gerar o HTML/CSS dos templates: Podem pedir à IA para "criar um HTML bonito com CSS/Bootstrap para uma lista de produtos" ou "estilizar este formulário". Nosso foco agora é no back-end (Django/Python).

❌ NÃO PERMITIDO:

Pedir à IA para gerar a lógica completa: "Escreva a view de cadastro de equipamento do Django".

Pedir para fazer os models: "Faça o models.py para um sistema de inventário".

O código de lógica (Python, views, forms, models) deve ser escrito por vocês.

✅ Meta de Conclusão da Fase 1
O projeto está concluído quando um usuário consegue, sem acessar o /admin:

Acessar a página de listagem.

Clicar em um link "Cadastrar Novo Equipamento".

Preencher o formulário e salvar.

Ser redirecionado para a lista e ver o novo item que acabou de cadastrar.

Clicar em qualquer item da lista e ver sua página de detalhes.

Façam um repositorio no github com o nome "Projeto Django". A cada etapa concluída deverá ser feito um commit, até o fim do projeto