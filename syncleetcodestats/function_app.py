import azure.functions

app = azure.functions.FunctionApp()

@app.function_name(name="syncleetcodestats")
@app.route(route="req")
def main(req: azure.functions.TimerRequest) -> str:
    user = req.params.get('user')
    return f'Hello, {user}!'