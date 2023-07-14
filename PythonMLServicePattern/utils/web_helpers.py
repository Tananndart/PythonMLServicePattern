import io


async def get_form_data_parameter(parameter_name, request):
    reader = await request.multipart()

    while True:
        field = await reader.next()

        if field is None:
            break

        if field.name == parameter_name:
            if field.filename:
                try:
                    file_content = await field.read(decode=False)
                    return io.BytesIO(file_content)
                except Exception as e:
                    print(f'File processing error: {e}')
                    return None

            value = await field.text()
            return value

    return None
