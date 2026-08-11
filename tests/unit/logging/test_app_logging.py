from __future__ import annotations

import logging

import pytest

from src.shared.logging.factory import init_logger


@pytest.mark.unit
def test_init_logger_configures_stdout_and_file_handlers(tmp_path, capsys) -> None:
    log_file = tmp_path / "app.log"
    init_logger()

    logger = logging.getLogger(__name__)
    logger.debug("debug-message")
    logger.info("info-message")

    stdout_text = capsys.readouterr().out
    file_text = log_file.read_text(encoding="utf-8")

    assert "info-message" in stdout_text
    assert "debug-message" not in stdout_text
    assert "info-message" in file_text
    assert "debug-message" in file_text


@pytest.mark.unit
def test_init_logger_handler_levels(tmp_path) -> None:
    root_logger = init_logger()

    file_handlers = [handler for handler in root_logger.handlers if isinstance(handler, logging.FileHandler)]
    stream_handlers = [
        handler
        for handler in root_logger.handlers
        if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler)
    ]

    assert root_logger.level == logging.DEBUG
    assert len(file_handlers) == 1
    assert len(stream_handlers) == 1
    assert file_handlers[0].level == logging.DEBUG
    assert stream_handlers[0].level == logging.INFO

