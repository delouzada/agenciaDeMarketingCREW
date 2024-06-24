from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from agencia_marketing.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

from langchain_google_genai import ChatGoogleGenerativeAI
import os

# COLE A CHAVE DO GOOGLE AQUI
GOOGLE_API_KEY = "CHAVE GOOGLE"

# Cria uma instância do modelo Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5,
    google_api_key=GOOGLE_API_KEY
)

@CrewBase
class AgenciaMarketingCrew():
	"""AgenciaMarketing crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def pesquisador(self) -> Agent:

		return Agent(
			config=self.agents_config['pesquisador'],
			llm=llm,
			verbose=True
		)
	@agent
	def estrategista(self) -> Agent:

		return Agent(
			config=self.agents_config['estrategista'],
			verbose=True,
			llm=llm
		)
	@agent
	def copywriter(self) -> Agent:

		return Agent(
			config=self.agents_config['copywriter'],
			verbose=True,
			llm=llm
		)
	@agent
	def gestor(self) -> Agent:

		return Agent(
			config=self.agents_config['gestor'],
			verbose=True,
			llm=llm
		)
	@task
	def pesquisador_task(self) -> Task:

		return Task(
			config=self.tasks_config['pesquisador_task'],
			agent=self.pesquisador()

		)
	@task
	def estrategista_task(self) -> Task:

	    return Task(
			config=self.tasks_config['estrategista_task'],
			agent=self.estrategista(),
			output_file='trabalho.md'

		)

	@task
	def copywriter_task(self) -> Task:
		return Task(
			config=self.tasks_config['copywriter_task'],
			agent=self.copywriter()


		)
	@task
	def gestor_task(self) -> Task:

		return Task(
			config=self.tasks_config['gestor_task'],
			agent=self.gestor()

		)
	@crew
	def crew(self) -> Crew:
		#"""Creates the AgenciaMarketing crew"""#

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)