import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
 // app.enableCors({
  //  origin: 'http://127.0.0.1:8000',
  //  credentials: true,
app.enableCors({
  origin: true,
  credentials: true,
});
  
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
