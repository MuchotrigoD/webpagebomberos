import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { Curso } from './cursos/curso.entity';
import { Noticia } from './noticias/noticia.entity';
import { Postulacion } from './postulaciones/postulacion.entity';
import { Usuario } from './usuarios/usuario.entity';
import { UsuariosController } from './usuarios/usuarios.controller';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: parseInt(process.env.DB_PORT || '5432', 10),
      username: process.env.DB_USERNAME,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_DATABASE,
      entities: [Curso, Noticia, Postulacion, Usuario],
      synchronize: true,
      autoLoadEntities: true,
    }),
    TypeOrmModule.forFeature([Curso, Noticia, Postulacion, Usuario]),
  ],
  controllers: [AppController, UsuariosController],
  providers: [AppService],
})
export class AppModule {}
