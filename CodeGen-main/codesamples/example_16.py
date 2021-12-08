def extract_crypto_data(github_path):
    """
    github_path can must be path on github, such as
    "bitcoin/bitcoin" or "litecoin-project/litecoin"
    """
    data = {'github_link': 'https://github.com/%s' % github_path}

    content = get_content_from_github(github_path, "chainparams.cpp")
    if content:
        data.update(_get_from_chainparams(content))
    else:
        content = get_content_from_github(github_path, "base58.h")
        if content:
            data.update(_get_from_base58h(content))

    content = get_content_from_github(github_path, "main.cpp")
    if content:
        data.update(_get_from_main(content))

    return data