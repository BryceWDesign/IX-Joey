# IX-Joey AI

IX-Joey is an advanced modular AI language model designed to operate with a dynamic,
specialized knowledge system. Joey can seamlessly connect to IX-Gibson — a powerful
central knowledge hub — to request domain-specific expert answers, enabling flexible,
scalable, and highly knowledgeable AI behavior.

---

## Gibson Connection Overview

- IX-Joey integrates the `GibsonAdapter` to communicate exclusively with IX-Gibson.
- User inputs formatted as `Ask <domain>: <question>` are routed to Gibson for expert
  answers.
- IX-Joey acts as a frontline interface, delegating complex, domain-specific queries
  to Gibson, allowing Joey to maintain focus on conversational context and general
  reasoning.
- Only IX-Joey is authorized to initiate communication with IX-Gibson; other AI repos
  operate independently and do not interact directly.
- This modular design improves scalability, reduces overhead, and allows a hive-mind
  structure where IX-Gibson acts as the knowledge nucleus.

---

## Philosophy

> “Well you guys always think he should know everything; you never tell him anything.”  
> — Joey, inspired by *Hackers* (1995)

IX-Joey is named after the character Joey from the film *Hackers*, symbolizing an AI
that learns from every interaction and grows through modular knowledge sharing, rather
than a monolithic static model.

---

## Getting Started

1. Ensure IX-Gibson is running and accessible at the configured API endpoint.
2. Run the `joey_interface.py` to start the command line interface.
3. Use the format `Ask <domain>: <question>` to query expert domains via Gibson.
4. Type `exit` or `quit` to stop the session.

---

## Architecture

- `core/gibson_adapter.py` — Handles communication with IX-Gibson API.
- `core/joey_core.py` — Main reasoning engine with Gibson query parsing.
- `core/joey_interface.py` — User interaction layer.
- `config/gibson_config.py` — Centralized Gibson connection settings.
- `utils/gibson_comm.py` — Robust communication utilities with retry logic.
- `core/gibson_integration.py` — Centralizes Gibson request/response management.

---

## License

Licensed under the Apache License 2.0.

---

## Contact

For questions, reach out via the IX-Joey GitHub repo issues or contact the development team.

