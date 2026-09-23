Gerador de Senhas

1. Project Overview

This project is a personal password generator developed in Python.

Its purpose is to simplify the creation of unique passwords for
different websites and services while keeping a simple record of
generated passwords.

The project was created as a personal software-development exercise and
as a practical utility.

The current repository contains:

README.md

gerador_senha.py

The existing application is a desktop graphical application.

The repository README describes the application as a "Gerador de Senhas
Inteligente", with the objective of generating secure and unique
passwords from a simple and efficient logic.

2. Current User Experience

The current interface contains the following main concepts:

URL or name of the website/service

Button to generate the password

Display of the generated password

History of generated passwords

Button to clear the password history

The visible interface includes labels similar to:

Gerador Automático de Senhas

URL ou nome do site:

Gerar Senha

Senha Gerada:

Histórico de Senhas Geradas:

Limpar Histórico

The site/service name is an important input because the application is
intended to help generate a distinct password for each website or
system.

3. Technology

The current project is implemented in:

Python

The main source file is:

gerador_senha.py

Do not assume the project uses a web framework.

Do not migrate the application to React, Node.js, Flask, Django or
another framework unless the user explicitly requests it.

If the existing Python file uses a specific GUI toolkit or
standard-library module, inspect the source before changing the
technology.

4. Main Functional Requirements

The application should preserve these core capabilities:

4.1 Website/service input

The user enters a URL, domain, website name or service name.

Examples:

github.com

LinkedIn

Gmail

Meu Sistema

Sistema ERP

The input is used as contextual information for the generated password
and/or history.

Do not assume that the URL itself must be used as a password seed unless
the existing implementation explicitly does so.

4.2 Password generation

The application generates a password when the user clicks:

Gerar Senha

The generated password should be:

Unique when possible

Random

Difficult to guess

Appropriate for use on websites and systems

Displayed clearly to the user

Do not claim that a generated password is cryptographically secure
unless the implementation uses a cryptographically appropriate random
source.

For security-sensitive password generation in Python, prefer the
secrets module over random when implementing or modernizing the
generator.

5. Password Generation Rules

When changing the generation algorithm, prioritize security over
superficial complexity.

A strong password generator should consider:

Sufficient length

Uppercase letters

Lowercase letters

Numbers

Special characters

Avoidance of predictable sequences

Avoidance of repeated deterministic patterns

If the project already has an established character set or password
length, preserve it unless the user asks to change it.

Do not silently change the generated-password format because existing
users may rely on it.

6. Site-Specific Passwords

The project is intended to help the user maintain different passwords
for different sites/services.

The site/service identifier should therefore remain associated with the
generated password in the history when the current implementation
supports this.

Example conceptual record:

Site: GitHub
Password: ********

Do not expose passwords unnecessarily in logs, screenshots or debugging
output.

7. Password History

The interface currently provides a history area for generated passwords.

The history should:

Show generated records clearly.

Preserve the association between site/service and password when
applicable.

Be easy to read.

Avoid accidental deletion.

Allow the user to clear the history explicitly.

The Limpar Histórico action is destructive for the local history and
should remain an explicit user action.

Do not clear the history automatically after generating a password.

8. Data Persistence

Before changing how the history is stored, inspect the existing
implementation.

Do not assume the history is persisted between application executions.

If the current implementation stores history only in memory, preserve
that behavior unless persistence is explicitly requested.

If persistence is added, prefer a simple local storage mechanism
appropriate for a small desktop application.

Potential options include:

JSON

SQLite

Do not introduce a database server for this application without a clear
requirement.

9. Security and Privacy

This project deals with passwords and therefore must be treated as
security-sensitive.

Never:

Commit real passwords to GitHub.

Store test credentials in source code.

Print generated passwords to console logs unnecessarily.

Send passwords to external APIs.

Upload passwords to cloud services without explicit user consent.

Include passwords in analytics.

Include passwords in error messages.

Expose password history in public screenshots.

If password history is persisted locally, protect it appropriately.

A future secure version should consider:

Local encryption

OS credential/keychain storage

Password visibility controls

Clipboard protection

Automatic history expiration

Do not implement encryption incorrectly just to claim that data is
encrypted.

10. Clipboard

If a future version adds a "Copy password" feature:

Copy only the currently generated password.

Do not copy the entire history.

Provide clear visual feedback.

Consider clearing the clipboard after a configurable period.

Do not log clipboard contents.

Clipboard functionality should be explicit and user-controlled.

11. GUI Principles

The current application is a simple utility.

The interface should prioritize:

Simplicity

Speed

Readability

Security

Clear feedback

The primary workflow should remain obvious:

Site / Service
      ↓
Generate Password
      ↓
Password Generated
      ↓
Password History

Avoid unnecessary screens.

Avoid excessive animations.

Avoid adding complexity that does not improve the password-generation
workflow.

12. UI Modernization

If redesigning the interface, preserve the existing mental model.

The redesigned interface should still contain:

Input

Website/service identifier.

Primary action

Generate password.

Result

Clearly display the generated password.

History

Show previously generated records.

Destructive action

Clear history.

A modern UI can improve:

Typography

Spacing

Visual hierarchy

Password visibility

Copy interaction

Responsive layout

But it should not remove the core workflow.

13. If Used With Lovable

Lovable can be used to create a modern web interface or prototype for
this project.

When doing so:

Treat the existing Python project as the source of truth for current
behavior.

Preserve the core user workflow.

Do not invent functionality that does not exist.

Do not assume that Python code can execute directly inside the
browser.

Do not assume that a web application can safely store passwords
without defining a storage/security architecture.

Do not send passwords to a backend unnecessarily.

Prefer client-side generation for a browser-based password generator
when appropriate.

Use a cryptographically appropriate browser random source for
security-sensitive generation.

Clearly separate UI from password-generation logic.

Do not migrate the existing project automatically without explicit
approval.

14. Web Version Architecture

If the project is migrated to a web application, the preferred
conceptual architecture is:

User
  ↓
Web UI
  ↓
Password Generator
  ↓
Secure Random Source
  ↓
Generated Password
  ↓
Optional Local History

For a simple password generator, a backend is not inherently required.

If history is kept locally, consider browser-local storage rather than
sending passwords to a server.

If a backend is introduced, the security model must be explicitly
defined before implementation.

15. Password History in a Web Version

For a web version, local history should be preferred over remote
persistence when the feature does not require synchronization.

Possible browser-side storage:

localStorage for non-sensitive prototype data

IndexedDB for larger structured local data

However, storing plaintext passwords in browser storage creates security
risks.

For a security-focused version, consider:

No persistent password history by default.

Optional encrypted local vault.

Explicit user unlock.

Strong master-password-derived encryption.

Clear-all functionality.

Do not implement a fake encryption layer.

16. Password Strength

If a password-strength indicator is introduced, it should be based on
transparent criteria.

Possible factors:

Length

Character diversity

Repetition

Predictability

Common-password detection

Avoid presenting a simplistic "100% secure" claim.

A strength meter is an estimate, not a guarantee of security.

17. Input Validation

The site/service field should accept reasonable input such as:

Domain names

URLs

Application names

System names

Do not unnecessarily reject values merely because they are not valid
URLs if the product explicitly supports names.

Trim unnecessary whitespace.

Handle empty input gracefully.

If the input is required for generation, provide clear feedback instead
of silently generating a password.

18. Error Handling

Expected situations include:

Empty site/service input.

Password generation failure.

Invalid configuration.

History storage failure.

Local storage unavailable.

Clipboard access denied.

Errors should:

Be understandable.

Not expose sensitive information.

Not reveal generated passwords.

Allow the user to recover.

19. Code Organization

The current repository is intentionally small.

Do not create unnecessary architecture.

For a small Python application, a reasonable future structure could be:

Gerador-de-Senhas/
│
├── gerador_senha.py
├── password_generator.py
├── history_manager.py
├── README.md
└── tests/

Only split files when the code has grown enough to justify it.

The password-generation algorithm should ideally be independent from the
GUI so it can be tested separately.

20. Testing

When modifying password generation, test:

Basic generation

Password is generated.

Password is not empty.

Password length is correct.

Character requirements

When configured:

Uppercase characters are supported.

Lowercase characters are supported.

Numbers are supported.

Special characters are supported.

Randomness

Consecutive generations should normally differ.

The generator should not create deterministic predictable sequences.

Input

Empty site/service is handled.

Whitespace is handled.

Long names are handled.

Special characters in site names are handled.

History

Generated records appear.

Multiple sites can be represented.

Clear history works explicitly.

Clearing history does not break future generation.

21. Security Testing

Before calling the application secure, verify:

Passwords are generated with an appropriate random source.

No plaintext credentials are embedded in source code.

Passwords are not logged.

Passwords are not sent externally.

Persistent history is understood and protected.

Clipboard behavior is controlled.

Error messages do not expose secrets.

Do not use the phrase "secure password generator" as a technical
guarantee unless the implementation supports that claim.

22. Change Management

For any significant feature, document:

Problem

What user problem is being solved?

Current behavior

What does the application do today?

New behavior

What changes?

Files affected

Which files are modified?

Security impact

Does the change affect password generation, storage, clipboard or
privacy?

Validation

How was the feature tested?

23. Do Not Rewrite Working Functionality

This is an existing personal project.

When modifying it:

Inspect the current implementation first.

Preserve working behavior.

Avoid unrelated refactoring.

Avoid changing the password-generation algorithm without
understanding it.

Avoid introducing dependencies without reason.

Avoid replacing the GUI toolkit without explicit approval.

If a modernization is requested, propose the migration before performing
it.

24. Important Rule for AI Agents

Never infer security properties from the project name or README alone.

For example:

Do not assume:

Cryptographic randomness

Encryption

Secure password storage

Secure password history

Secure clipboard handling

These properties must be verified in the implementation.

The source code is the authority.

25. Definition of Done

A change is complete when:

The requested feature works.

Existing password generation still works.

Existing history behavior still works.

No password is accidentally exposed.

No unnecessary dependency was introduced.

The application remains simple to use.

Security implications of the change have been considered.

The implementation has been tested.

26. Guiding Principle

The project should remain a simple and useful password-generation
utility.

The primary objective is:

Generate unique passwords quickly for different websites and services
while minimizing unnecessary exposure of sensitive password data.

When improving the project, favor:

Security → Simplicity → Usability → Visual polish

and avoid adding complexity without a concrete user benefit.
