<div align="center">

# 🚀 Sistema Jotta — Arquitetura de BI e Engenharia de Dados

**Solução completa de dados: da modelagem relacional ao dashboard executivo**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

## 🎯 O Problema de Negócio

Empresas de e-commerce frequentemente enfrentam **inconsistências financeiras** — faturamento alto sem clareza sobre rentabilidade real. Este projeto resolve esse problema construindo uma arquitetura de dados completa, do zero, capaz de processar **R$ 53,25 milhões em transações** e entregar KPIs confiáveis para tomada de decisão.

---

## 🛠️ Stack Utilizada

| Camada | Tecnologia |
|--------|-----------|
| Banco de Dados | Supabase (PostgreSQL) |
| Engenharia de Dados | Python · Pandas · SQLAlchemy |
| Visualização | Power BI (DAX · Star Schema) |
| Automação | Scripts de Carga Massiva |

---

## 📂 Estrutura do Projeto

```
projeto-ecommerce-python/
│
├── estrutura_banco.sql       → Modelagem das tabelas e relacionamentos
├── povoamento_dados.py       → Carga das tabelas dimensionais
├── sistema_jotta_vendas.py   → Motor de vendas e regras de negócio
├── carga_massiva.py          → Simulação de escala com milhares de transações
│
├── Dashboard_python1.png     → Visão geral financeira
├── Dashboard_python20.png    → Performance operacional e despesas
└── Dashboard_python3.png     → Detalhamento de vendas
```

---

## ⚙️ Infraestrutura e Engenharia de Dados

### 1. `estrutura_banco.sql` — Modelagem do Banco
Define a arquitetura das tabelas (Produtos, Filiais, Vendas) no Supabase. Implementação de chaves primárias e estrangeiras para garantir integridade referencial, permitindo que o Power BI identifique os relacionamentos automaticamente.

[📄 Ver arquivo](./estrutura_banco.sql)

---

### 2. `povoamento_dados.py` — Povoamento Inteligente
Script Python responsável por alimentar as tabelas dimensionais (Produtos e Filiais). Garante que cada produto tenha atributos específicos (preço, categoria) e cada filial tenha seus custos fixos (aluguel, manutenção) devidamente registrados para o cálculo de margem posterior.

[📄 Ver arquivo](./povoamento_dados.py)

---

### 3. `sistema_jotta_vendas.py` — Motor de Vendas e Métricas
O "cérebro" da operação. Integra as regras de negócio das métricas de e-commerce com o fluxo de vendas. Destaque: cálculo dinâmico de impostos e taxas de entrega antes da carga no banco de dados.

[📄 Ver arquivo](./sistema_jotta_vendas.py)

---

### 4. `carga_massiva.py` — Simulação de Escala
Script de estresse para povoar o banco com milhares de transações reais. Foi através deste script que geramos os **R$ 53,25 milhões em faturamento**, provando que a solução é escalável para grandes volumes.

[📄 Ver arquivo](./carga_massiva.py)

---

## 📊 Dashboards — Resultados Finais

### 1. Visão Geral Financeira
Foco no monitoramento de KPIs macro: Receita Bruta, Volume de Transações e Lucro Líquido consolidado.

![Dashboard Visão Geral](./Dashboard_python1.png)

---

### 2. Performance Operacional e Despesas
Análise de custos fixos vs. variáveis, ranking de rentabilidade por estado e eficiência por categoria de produto.

![Dashboard Performance](./Dashboard_python20.png)

---

### 3. Detalhamento e Registro de Vendas
Visão granular dos dados, exibindo a integridade de cada registro transacional processado pelo sistema.

![Dashboard Detalhamento](./Dashboard_python3.png)

---

## 🔑 Principais Resultados

- ✅ Pipeline end-to-end funcional do banco ao dashboard
- ✅ R$ 53,25 milhões em faturamento simulado e processado
- ✅ Star Schema implementado para performance no Power BI
- ✅ Cálculo automático de impostos, margem e custos fixos por filial
- ✅ Arquitetura escalável validada com carga massiva de dados

---

## 👤 Autor

**João Marcos** — Data Analyst | Power BI · Python · SQL

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joão-marcos-347311230)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JottaMarcos)
