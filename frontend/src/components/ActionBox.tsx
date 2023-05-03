import type { MouseEvent } from "react"

import { recordClickEvent, selectAction } from "../Api"
interface ActionBoxInterface {
  action: Action
  userId: string
  validAction: boolean
  fetchMessages: () => void
}

export default function ActionBox({
  action,
  userId,
  validAction,
  fetchMessages,
}: ActionBoxInterface) {
  const isLink: boolean = !!action.redirect
  const textDisplay = isLink ? "🔗  " + action.text : action.text

  const handleClick = async (event: MouseEvent<HTMLButtonElement>) => {
    recordClickEvent(userId, action.id)
    if (!isLink) {
      event.preventDefault()
      await selectAction(userId, action.id)
      fetchMessages()
    }
  }

  let button

  if (isLink) {
    button = (
      <button onClick={handleClick}>
        <a href={action.redirect} target="_blank">
          {textDisplay}
        </a>
      </button>
    )
  } else if (validAction) {
    button = <button onClick={handleClick}>{textDisplay}</button>
  } else {
    button = <div>{textDisplay}</div>
  }

  return (
    <div className="w-fit rounded-xl px-4 py-1 text-sm text-blue-500 bg-green-400 shadow-sm">
      {button}
    </div>
  )
}
