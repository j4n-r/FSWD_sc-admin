{
  description = "Python env";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.systems.url = "github:nix-systems/default";
  inputs.flake-utils = {
    url = "github:numtide/flake-utils";
    inputs.systems.follows = "systems";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            (pkgs.python313.withPackages (
              python-pkgs: with python-pkgs; [
                flask
                flask-jwt-extended
                flask-cors
                flask-wtf
                wtforms
                python-dotenv
              ]
            ))
            pkgs.sqlite

            pkgs.tailwindcss
            pkgs.tailwindcss-language-server
            pkgs.nodePackages_latest.tailwindcss
          ];
          env = {
            PYRIGHT_PYTHON_PATH = "${pkgs.python312}/bin/python3";
            #WS_URL = ""; # 0.0.0.0:8080 is in python app defined, used only for deployments
          };
        };
      }
    );
}
