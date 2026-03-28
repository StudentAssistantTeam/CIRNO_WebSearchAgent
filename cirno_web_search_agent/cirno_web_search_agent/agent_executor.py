import logging
# a2a dependencies
from a2a.server.tasks import TaskUpdater
from a2a.server.agent_execution import (
    AgentExecutor,
    RequestContext
)
from a2a.server.events import EventQueue
from a2a.utils import (
    new_task,
    new_agent_text_message
)
from a2a.utils.errors import (
    ServerError,
    UnsupportedOperationError
)
from a2a.types import (
    InternalError,
    TaskState,
    Part,
    TextPart
)
# Project dependencies
from cirno_web_search_agent.agent import agent

logger = logging.getLogger("agent executor")
agent_instance = agent()


# Agent Executor
class agent_executor(AgentExecutor):
    def __init__(self):
        self.agent = agent_instance

    # Agent Execution
    async def execute(
            self,
            context: RequestContext,
            event_queue: EventQueue
    ):
        query = context.get_user_input()
        task = context.current_task
        if not task:
            task = new_task(context.message)
            await event_queue.enqueue_event(task)
        # updater
        updater = TaskUpdater(event_queue, task.id, task.context_id)
        try:
            # initialization
            await self.agent.initialize()
            # Streaming
            async for chunk in self.agent.streaming(query, task.context_id):
                # check whether it is done
                is_done = chunk.done
                if not is_done:
                    if chunk.step != "model":
                        continue
                    # Updating task
                    await updater.update_status(
                        TaskState.working,
                        new_agent_text_message(
                            chunk.content,
                            context_id=task.context_id,
                            task_id=task.id
                        )
                    )
                else:
                    await updater.add_artifact(
                        [Part(root=TextPart(text=chunk.content))],
                        name="conversation_result"
                    )
                    await updater.complete()
                    break
        except Exception as e:
            # Error handling
            logger.error(f"Agent execution failed due to {e}")
            raise ServerError(error=InternalError()) from e

    # Cancelling
    async def cancel(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        logger.error("Unsupported operation")
        raise ServerError(error=UnsupportedOperationError())
