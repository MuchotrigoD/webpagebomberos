import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from 'typeorm';

@Entity()
export class Noticia {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ length: 200 })
  titulo: string;

  @Column({ type: 'text' })
  contenido: string;

  @Column({ nullable: true })
  imagenUrl: string;

  @Column({ type: 'date' })
  fecha: string;

  @CreateDateColumn({ name: 'creado_en' })
  creadoEn: Date;
}
