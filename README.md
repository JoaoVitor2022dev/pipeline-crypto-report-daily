# 📈 Crypto Automated Reporting Pipeline (CARP)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)

## 📋 Sobre o Projeto
Este projeto não é apenas um script de coleta de dados; é uma **solução de Business Intelligence de ponta a ponta**. Ele automatiza a extração de dados críticos do mercado de criptomoedas, realiza o tratamento dos dados e garante que a informação chegue ao tomador de decisão no canal mais ágil possível: o WhatsApp.

### 🎯 Por que isso é "Outro Nível"?
No mercado corporativo, o dado parado não tem valor. Esta solução resolve três problemas principais:
1. **Extração (ETL):** Consumo direto de APIs REST confiáveis.
2. **Governança:** Organização automática de arquivos em diretórios datados, facilitando auditorias futuras.
3. **Comunicação Ativa:** Diferente de dashboards passivos que dependem do usuário logar para ver, aqui o dado "vai até o cliente".

---

## 🚀 Funcionalidades
- **Data Sourcing:** Conexão com a API CoinGecko para monitoramento das Top 10 moedas por Market Cap.
- **Data Transformation:** Limpeza e renomeação de campos técnicos para termos de negócio (Business Rules).
- **Storage:** Exportação automatizada para formato `.xlsx` com versionamento por data.
- **Alert System:** Notificação instantânea via WhatsApp Web utilizando `pywhatkit`.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**: Linguagem base.
- **Pandas**: Manipulação e análise de dados estruturados.
- **Requests**: Interface com a API REST.
- **PyWhatKit**: Automação de interface para mensageria.
- **OpenPyXL**: Engine de suporte para escrita de arquivos Excel.

---

## ⚙️ Como Executar

Instale as dependências:

Bash
pip install pandas requests pywhatkit openpyxl
Configure o caminho do diretório no script para sua realidade local.

Execute o script:

Bash
python main.py
Nota: Para o envio do WhatsApp, certifique-se de estar com o WhatsApp Web logado no seu navegador padrão.

📈 Próximos Passos (Roadmap)
[ ] Integração com SQL Server para persistência histórica dos dados (seu foco atual!).

[ ] Implementação de logs de erro para garantir a resiliência da automação.

[ ] Criação de um executável (.exe) para rodar em background.

✨ Projeto desenvolvido para fins de estudo e automação de processos em 2026.


---

## 3. Dica de Ouro: O toque de SQL Server

Como você está estudando **SQL Server**, o seu próximo passo para esse repositório brilhar ainda mais é criar um script `.sql` que cria uma tabela chamada `Historico_Cripto`. 

Em vez de só salvar no Excel, você poderia usar a biblioteca `sqlalchemy` ou `pyodbc` para inserir esses mesmos dados no banco. Isso mostra que você sabe lidar com **Arquitetura de Dados**.

**O que você acha de eu te ajudar a criar a parte desse script que conecta no SQL Serve
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/crypto-automation-tracker.git](https://github.com/seu-usuario/crypto-automation-tracker.git)
