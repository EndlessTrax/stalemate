from stalemate import archives


if __name__ == "__main__":
    username = "endlesstrax"

    url = archives.build_archive_endpoint(username)
    user_archives = archives.fetch_archives_list(url)

    print(user_archives)