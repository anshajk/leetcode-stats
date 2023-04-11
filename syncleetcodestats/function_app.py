import azure.functions

app = azure.functions.FunctionApp()


@app.function_name(name="syncleetcodestats")
@app.schedule(schedule="0 */5 * * * *", arg_name="mytimer", run_on_startup=True)
def main(req: azure.functions.TimerRequest) -> str:
    print("Function executed")
