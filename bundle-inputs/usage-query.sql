-- Usage rows for the news-image-20261120 build session only.
-- The query is the one bundle --help prints (step 1), with the model
-- joined in. Run it with the muse.db tool AFTER the build session has
-- ended: Muse writes a message's usage row when the message is
-- delivered, and the session's row appears only once the session ends.
-- At bundle time (session still running) this query returned 0 rows,
-- so usage.jsonl beside this file starts empty; re-run the query and
-- re-bundle once the session is over.
SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('fedf6c95-6d50-490a-ae46-80102d6efcb0') ORDER BY u.created_at DESC LIMIT 500
