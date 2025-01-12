from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tools.custom_tool import CustomSerperDevTool
from crewai_tools import TXTSearchTool
import os
from langchain_groq import ChatGroq
from composio_crewai import ComposioToolSet, Action, App

# List of tools
composio_toolset = ComposioToolSet()
create_gc_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])
find_gc_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_EVENT'])
update_gc_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_UPDATE_EVENT'])
delete_gc_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_DELETE_EVENT'])
weather_tool = composio_toolset.get_tools(actions=['WEATHERMAP_WEATHER'])
gmail_send_tool = composio_toolset.get_tools(actions=['GMAIL_SEND_EMAIL'])
gmail_draft_tool= composio_toolset.get_tools(actions=['GMAIL_CREATE_EMAIL_DRAFT'])
gmail_fetch_tool = composio_toolset.get_tools(actions=['GMAIL_FETCH_EMAILS'])

Reader_tool = TXTSearchTool(txt='D:/Personal_Assistant/myproject/combined_transcript.txt',
    config={
        "llm": {
            "provider": "groq",  # Other options include google, openai, anthropic, llama2, etc.
            "config": {
                "model": "groq/mixtral-8x7b-32768",
            },
        },
        "embedder": {
            "provider": "cohere",
        "config": {
            "model": "embed-english-v3.0",
            "api_key":os.environ["COHERE_API_KEY"],
        }
        },
    }
)

llm = ChatGroq(model="groq/llama3-8b-8192", api_key=os.environ["GROQ_API_KEY"])


@CrewBase
class Myproject():
    """AI_Personal_Assistant"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # @agent
    # def researcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['researcher'],
    #         tools=[CustomSerperDevTool(), ScrapeWebsiteTool()],
    #         verbose=True,
    #         allow_delegation=True,
    #         rpm=3
    #     )

    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'],
    #         verbose=True,
    #         allow_delegation=True,
    #         rpm=3
    #     )

    # @agent
    # def news_reporter(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['news_reporter'],
    #         verbose=True,
    #         allow_delegation=True,
    #         rpm=3
    #     )

    @agent
    def create_event_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['create_event_agent'],
            tools=[create_gc_event_tool[0]],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )

    @agent
    def find_event_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['find_event_agent'],
            tools=[find_gc_event_tool[0]],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )

    @agent
    def update_event_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['update_event_agent'],
            tools=[update_gc_event_tool[0]],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )

    @agent
    def delete_event_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['delete_event_agent'],
            tools=[delete_gc_event_tool[0]],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )
 
    @agent
    def retriever_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['retriever_agent'],
            tools=[Reader_tool],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )
    @agent
    def question_answering_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['question_answering_agent'],
            tools=[search_tool],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )
    
    @agent
    def summarise_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarise_agent'],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )

    @agent
    def gmail_create_draft_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['gmail_create_draft_agent'],
            verbose=True,
            tools=[gmail_draft_tool[0]],
            allow_delegation=True,
            rpm=3
        )

    @agent
    def gmail_send_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['gmail_send_agent'],
            verbose=True,
            tools=[gmail_send_tool[0]],
            allow_delegation=True,
            rpm=3
        )
        
    @agent
    def gmail_fetch_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['gmail_fetch_agent'],
            verbose=True,
            tools=[gmail_fetch_tool[0]],
            allow_delegation=True,
            rpm=3
        )

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            verbose=True,
            tools=[weather_tool[0]],
            allow_delegation=True,
            rpm=3
        )

    @agent
    def weather_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_reporter'],
            verbose=True,
            allow_delegation=True,
            rpm=3
        )


    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['research_task'],
    #         tools=[CustomSerperDevTool(), ScrapeWebsiteTool()],
    #     )

    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'],
    #         context=[self.tasks_config['research_task']]
    #     )

    # @task
    # def news_reporter_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['news_reporter_task'],
    #         context=[self.tasks_config['reporting_task']]
    #     )

    @task
    def task_create(self) -> Task:
        return Task(
            config=self.tasks_config['task_create'],
            tools=[create_gc_event_tool[0]]
        )

    @task
    def task_find(self) -> Task:
        return Task(
            config=self.tasks_config['task_find'],
            tools=[find_gc_event_tool[0]]
        )

    @task
    def task_update(self) -> Task:
        return Task(
            config=self.tasks_config['task_update'],
            tools=[update_gc_event_tool[0]]
        )

    @task
    def task_delete(self) -> Task:
        return Task(
            config=self.tasks_config['task_delete'],
            tools=[delete_gc_event_tool[0]]
        )
      
    @task
    def retrieve_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_task'],
            tools=[Reader_tool],
        )
    
    @task
    def question_answer_task(self) -> Task:
        return Task(
            config=self.tasks_config['question_answer_task'],
            tools=[search_tool],
            context=[self.tasks_config['retrieve_task']]
        )

    @task
    def summarise_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarise_task'],
            context=[self.tasks_config['retrieve_task']]
        )
        
    @task
    def task_create_draft(self) -> Task:
        return Task(
            config=self.tasks_config['task_create_draft'],
            tools=[gmail_draft_tool[0]]
        )

    @task
    def task_send_gmail(self) -> Task:
        return Task(
            config=self.tasks_config['task_send_gmail'],
            tools=[gmail_send_tool[0]]
        )

    @task
    def task_fetch_mails(self) -> Task:
        return Task(
            config=self.tasks_config['task_fetch_mails'],
            tools=[gmail_fetch_tool[0]]
        )

    @task
    def task_get_weather(self) -> Task:
        return Task(
            config=self.tasks_config['task_get_weather'],
            tools=[weather_tool[0]]
        )
        
    @task
    def task_get_report(self) -> Task:
        return Task(
            config=self.tasks_config['task_get_report'],
            context=[self.tasks_config['task_get_weather']]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AI_Personal_Assistant crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            # planning=True,
            # planning_llm=ChatGroq(model="groq/llama3-70b-8192", api_key=os.environ["GROQ_API_KEY"]),
            manager_llm=ChatGroq(model="groq/llama3-70b-8192", api_key=os.environ["GROQ_API_KEY"]),
            verbose=True,
        )