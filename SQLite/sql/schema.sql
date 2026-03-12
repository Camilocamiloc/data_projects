CREATE TABLE departamentos (
    Codigo INTEGER PRIMARY KEY,
    PaisCodigo INTEGER,
    Nombre TEXT
);

#-------------------------------------------------------------------------------

CREATE TABLE municipios (
    MunicipioCodigo INTEGER PRIMARY KEY,
    PaisCodigo INTEGER,
    DepartamentoCodigo INTEGER,
    Nombre TEXT,
    FOREIGN KEY (DepartamentoCodigo) REFERENCES departamentos(Codigo)
);

#-------------------------------------------------------------------------------

CREATE TABLE personas (
    personacodigo INTEGER PRIMARY KEY,
    primernombre TEXT,
    segundonombre TEXT,
    primerapellido TEXT,
    segundoapellido TEXT,
    cupototal REAL,
    cupodisponibletotal REAL,
    departamentocodigo INTEGER,
    municipiocodigo INTEGER,
    fechaexpedicion DATE,
    fechanacimiento DATE,
    genero TEXT,
    celular TEXT,
    personasacargo INTEGER,
    FOREIGN KEY (departamentocodigo) REFERENCES departamentos(Codigo),
    FOREIGN KEY (municipiocodigo) REFERENCES municipios(MunicipioCodigo)
);

#-------------------------------------------------------------------------------

CREATE TABLE almacenes (
    almacencodigo INTEGER PRIMARY KEY,
    nombre TEXT
);

#-------------------------------------------------------------------------------

CREATE TABLE creditos (
    personacodigo INTEGER,
    almacencodigo INTEGER,
    valorfactura REAL,
    fechacreacion DATE,
    saldocapital REAL,
    saldofinanciacion REAL,
    FOREIGN KEY (personacodigo) REFERENCES personas(personacodigo),
    FOREIGN KEY (almacencodigo) REFERENCES almacenes(almacencodigo)
);
