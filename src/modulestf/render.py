import glob
import json
import pathlib
import re
import shutil
from os import chdir, getcwd, makedirs, mkdir, path
from pprint import pformat, pprint

from cookiecutter.main import cookiecutter

from .const import COOKIECUTTER_TEMPLATES_DIR, OUTPUT_DIR, WORK_DIR, WORK_DIR_FOR_COOKIECUTTER, tmp_dir
from .logger import setup_logging
from .modules import MODULES

logger = setup_logging()


def mkdir_safely(dir):
    pass


def prepare_render_dirs():
    pass


def find_templates_files(dir):
    pass


def prepare_single_layer(resource, source_dir_name, region, templates_dir, templates_files):
    pass


# Copy all files and subdirectories into working directory
def copy_to_working_dir(templates_dir, work_dir=""):
    pass


def render_all(extra_context):
    pass


# Count unique combination of type and text to decide if to append unique resource id
def get_types_text(resources):
    pass


def make_dir_name(type, text, appendix=""):
    pass


# Update dynamic parameters with correct dir name
# Value to scan and replace can be inside of any structure (dict, list, string)
# Should start with "dependency."
#
# Examples:
# dependency.a3bfbba6-ff09-4efc-a56b-39b647f203f6.outputs.security_group_id => dependency.sg_2.outputs.security_group_id
# Source: https://stackoverflow.com/a/38970181/550451
def recursive_replace_dependency(input, dirs):
    pass


def render_from_modulestf_config(config, source, regions):
    pass
