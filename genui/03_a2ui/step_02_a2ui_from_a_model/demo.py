from agent import correction_loop,offline_messages
print('A2UI model lesson: OFFLINE FIXTURE (not a live model call)')
for item in correction_loop(offline_messages()): print(item)
