import { json } from '@sveltejs/kit'

export async function POST({ request }) {

    const { question, session_id } = await request.json()

    const response = await fetch(
        `http://127.0.0.1:8000/stream_answer?question=${encodeURIComponent(question)}&session_id=${session_id}`
    )

    const data = await response.json()

    return json({
        answer: data.answer,
        source: data.source
    })
}