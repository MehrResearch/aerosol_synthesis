FROM debian

ARG USER=developer
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y --no-install-recommends sudo git fish wget curl ca-certificates \
    && apt clean \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /usr/bin/fish ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER}


USER ${USER}
ARG HOME=/home/${USER}
WORKDIR ${HOME}

RUN <<EOT
    curl -LsSf https://astral.sh/uv/install.sh | sh
EOT
