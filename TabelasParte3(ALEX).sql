create table Disciplinas(
id int identity primary key not null,
nome varchar(80)not null,
data datetime,
status varchar(80)not null
check(status in('aberta','fechada')),
planodeensino char not null,
cargahoraria varchar(80)not null,
check((cargahoraria = 40 or cargahoraria=80)),
competencias varchar(80)not null,
habilidades varchar(80)not null,
ementa varchar(80)not null,
conteudoprogramatico varchar(80)not null,
bibliografiabasica varchar(80)not null,
bibliografiacomplementar varchar(80)not null,
percentualpratico int not null,
check(percentualpratico >= 0 or percentualpratico <=100),
percentualteorico int not null,
check(percentualteorico >= 0 or percentualteorico <=100),
);

create table solicitacaomatricula(
id int identity primary key not null,
dtsolicitacao datetime not null default(getdate()) ,
status varchar(250) not null default('Solicitada'),
check(status in('Solicitada','Aprovada','Rejeitada','Cancelada')),
--constraint datasolicitacao default(getdate()) for dtsolicitacao,
--constraint status default('Solicitada')for status,


);






