import openai


def get_car_ai_bio(model, brand, year):
    openai.api_key = 'SEUTOKENAQUI'

    prompt = f"""
    Me mostre um descrição de venda para o carro {model} {brand} {year} em apenas 250 caracteres. Fale coisas essenciais para venda.
    """
    respose = openai.completions.create(
        model='davinci-002',
        prompt=prompt,
        max_tokens=1000,
    )
    return respose