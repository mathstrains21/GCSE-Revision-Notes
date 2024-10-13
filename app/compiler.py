from pathlib import Path
from tomllib import load

from typing import List, Optional
from typing_extensions import Annotated

from typer import Typer, Argument

from .markdown import convert_to_markdown, get_data
from .html import render_data

app = Typer(no_args_is_help=True)

def compile(subject, topic):
    subject_folder = Path(subject)
    subject_source_folder = subject_folder / "src"
    with open(subject_source_folder / "config.toml", "rb") as f:
        subject_config = load(f)

    # Remove unnecessary data
    subject_config["papers"] = [paper for paper in subject_config["papers"] if topic in paper["topics"]]
    subject_config["topics"] = [topic_data for topic_data in subject_config["topics"] if topic_data["number"] == topic][0]

    topic_folder = subject_source_folder / "{number} {title}".format(**subject_config["topics"])
    with open(topic_folder / "config.toml", "rb") as f:
        topic_config = load(f)

    data = {
        "subject": subject_config,
        "topic": topic_config,
        "content": [
            {
                "type": "heading",
                "size": 1,
                "content": [{
                        "type": "text",
                        "content": topic_config["title"],
                }],
            },
        ],
    }

    markdown_files = ["# {title}".format(**topic_config)]

    for subtopic in topic_config["subtopics"]:
        subtopic_file = topic_folder / "{number} {title}.src.md".format(**subtopic)
        with open(subtopic_file) as f:
            subtopic_text = f.read()
        markdown_files.append(convert_to_markdown(subtopic_text))

        data["content"] += get_data(subtopic_text)



    markdown_content = "\n\n".join(markdown_files)
    html_content = render_data(data)

    # Create output folders if they don't already exist
    md_output_folder = subject_folder / "Markdown"
    md_output_folder.mkdir(exist_ok=True)

    html_output_folder = subject_folder / "HTML"
    html_output_folder.mkdir(exist_ok=True)

    # Write the compiled files
    with open(md_output_folder / "{number} {title}.md".format(**topic_config), "w") as f:
        f.write(markdown_content)

    with open(html_output_folder / "{number} {title}.html".format(**topic_config), "w") as f:
        f.write(html_content)

@app.command("topic")
def compile_topic(
        subject: Annotated[str, Argument(help="The subject to compile", show_default=False)],
        topics: Annotated[Optional[List[float]], Argument(help="The topics to compile", show_default="All topics")] = None,
    ):
    """
    Compile the listed topic's source files into HTML and Markdown files.
    """
    if topics is None:
        with open(Path(subject) / "src" / "config.toml", "rb") as f:
            subject_config = load(f)
        topics = [topic["number"] for topic in subject_config["topics"] if (Path(subject) / "src" / "{number} {title}".format(**topic) / "config.toml").exists()]
    for topic in topics:
        if int(topic) == topic:
            topic = int(topic)
        compile(subject, topic)

@app.callback()
def callback():
    """
    Compiles the source files for a subject into HTML and Markdown files.
    """
