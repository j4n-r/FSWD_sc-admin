{
  description = "Python env";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";
  inputs.nixpkgs-unstable.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  inputs.systems.url = "github:nix-systems/default";
  inputs.flake-utils = {
    url = "github:numtide/flake-utils";
    inputs.systems.follows = "systems";
  };

  outputs =
    {
      nixpkgs,
      nixpkgs-unstable,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pkgs-unstable = nixpkgs-unstable.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            (pkgs.python313.withPackages (
              python-pkgs: with python-pkgs; [
                flask
                flask-jwt-extended
                flask-cors
                python-dotenv
              ]
            ))
            pkgs.sqlite
            pkgs-unstable.opencode
          ];
          env = {
            PYRIGHT_PYTHON_PATH = "${pkgs.python312}/bin/python3";
            #WS_URL = ""; # defaults to 0.0.0.0:8080 in python app
          };
        };
      }
    );
}
